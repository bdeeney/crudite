from flask.app import Flask
from crudite.wrappers import Request, Response

__all__ = ['Crudite']


class Crudite(Flask):
    """Crudite application class."""
    request_class = Request
    response_class = Response

    def register_view(self, view_cls, endpoint, url, pk=None, pk_type=None):
        """Register a CruddyView on this app."""
        if pk is None:
            pk = view_cls.pk if view_cls.pk is not None else '_id'
        if pk_type is None:
            pk_type = view_cls.pk_type if view_cls.pk_type is not None \
                        else 'object_id'

        coll_methods = set(['POST', 'GET'])
        if view_cls.__methods__ is not None:
            coll_methods = coll_methods.intersection(view_cls.__methods__)

        entry_methods = set(['GET', 'PUT', 'DELETE'])
        if view_cls.__methods__ is not None:
            entry_methods = entry_methods.intersection(view_cls.__methods__)

        # register CREATE and INDEX operations on a collection resource
        collection_view = view_cls.as_view(endpoint + '_coll',
                                           resource_type='collection')

        self.add_url_rule(url, view_func=collection_view,
                          methods=coll_methods)

        # register READ, UPDATE, DELETE operations on an entry resource
        entry_url = '{url}<{pk_type}:{pk}>'.format(url=url, pk_type=pk_type,
                                                   pk=pk)
        entry_view = view_cls.as_view(endpoint + '_ent')
        self.add_url_rule(entry_url, view_func=entry_view,
                         methods=entry_methods)
