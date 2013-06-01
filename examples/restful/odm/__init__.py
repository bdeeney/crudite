import ming.schema as S
from ming.odm import (FieldPropertyWithMissingNone, ForeignIdProperty,
                      Mapper, RelationProperty, ThreadLocalORMSession, state)
from ming.odm.declarative import MappedClass

from restful.odm.session import session

__all__ = ['Field', 'Link', 'Mapper', 'Model', 'Relationship']


class Field(FieldPropertyWithMissingNone):

    def __init__(self, field_type, *args, **kwargs):
        kwargs.setdefault('if_missing', S.Missing)
        super(Field, self).__init__(field_type, *args, **kwargs)


class Link(Field, ForeignIdProperty):
    pass


class Relationship(RelationProperty):
    pass


class Model(MappedClass):
    """Base Model."""
    _id = Field(S.ObjectId)

    def __json__(self):
        """Return a JSON-serializable representation of the document."""
        return self.to_dict()
        
    def to_dict(self):
        """Return the current state of the document as a dict."""
        return state(self).document

    @property
    def created_at(self):
        """Return the document's generation time derived from the ObjectId."""
        return self._id.generation_time

Model.__mongometa__.session = session


def init_db(session):
    Mapper.compile_all()
    for mapper in Mapper.all_mappers():
        session.ensure_indexes(mapper.collection)
