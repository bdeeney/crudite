from flask import abort, current_app, request
from flask.views import View
from ming.odm import session
from ming.schema import Invalid
from werkzeug.utils import cached_property

from crudite.helpers import jsonify

__all__ = ['CruddyView', 'MingCruddyMixin', 'CruddyMingView']


class CruddyView(View):
    model = None
    pk = None
    pk_type = None
    _method_maps = {
        'collection': {'POST': 'create', 'GET': 'index'},
        'entry': {'GET': 'read', 'PUT': 'update', 'DELETE': 'delete'}
    }
    _status_code = {
        'POST': 201,    # Created
        'GET': 200,     # OK
        'PUT': 200,     # OK
        'DELETE': 204,  # No Content
    }

    __methods__ = None

    def __init__(self, **kwargs):
        super(CruddyView, self).__init__()
        self.resource_type = kwargs.pop('resource_type', 'entry')

    @cached_property
    def method_map(self):
        return self._method_maps.get(self.resource_type, {})

    @cached_property
    def methods(self):
        return self.method_map.keys()

    @cached_property
    def handler_name(self):
        return self.method_map[request.method]

    def dispatch_request(self, *args, **kwargs):
        handler = getattr(self, self.handler_name, None)
        if handler is None:
            raise NotImplementedError(self.handler_name)
        return self.process_return_value(handler(*args, **kwargs))

    def process_return_value(self, rv):
        """Render the view's return value as JSON."""
        if rv is None:
            return ''

        response_class = current_app.response_class
        if isinstance(rv, (response_class, basestring, tuple)) or callable(rv):
            return rv

        if self.handler_name == 'index':
            rv = {'entries': rv}
        elif hasattr(rv, 'to_dict') and callable(rv.to_dict):
            rv = rv.to_dict()

        return response_class(jsonify(rv), status=self.default_status,
                              mimetype='application/json')

    @cached_property
    def default_status(self):
        return self._status_code.get(request.method, None)


class MingCruddyMixin(object):

    def index(self, **kwargs):
        return self.model.query.find(kwargs).all()

    def create(self, **kwargs):
        try:
            entry = self.model(**request.json)
        except Invalid as exc:
            abort(400, exc.message)
        session(entry).flush()
        return entry

    def read(self, **kwargs):
        return self._get_entry(**kwargs)

    def update(self, **kwargs):
        entry = self._get_entry(**kwargs)
        entry.query.update({'$set': request.json}, safe=True, new=True)
        session(entry).flush()
        return entry

    def delete(self, **kwargs):
        entry = self._get_entry(**kwargs)
        entry.delete()
        session(entry).flush()

    def _get_entry(self, **kwargs):
        entry = self.model.query.get(**kwargs)
        if entry is None:
            abort(404)
        return entry


class CruddyMingView(CruddyView, MingCruddyMixin):
    pass
