from bson import ObjectId
from werkzeug.routing import BaseConverter


class ObjectIdConverter(BaseConverter):
    """A werkzeug converter to cast a URL element to an :class:`ObjectId`.
    """

    regex = '(?:[a-fA-F0-9]{24})'

    def to_python(self, value):
        return ObjectId(value)

    def to_url(self, value):
        return str(value)
