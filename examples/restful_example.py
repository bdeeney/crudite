from crudite.app import Crudite
from crudite.converters import ObjectIdConverter
from crudite.helpers import subscribe_logging_helpers

from restful.odm import init_db
from restful.odm.session import session
from restful.views import UserView, TemplateView, MessageView

init_db(session)

app = Crudite(__name__)
subscribe_logging_helpers(app)
app.url_map.converters['object_id'] = ObjectIdConverter

app.register_view(UserView, 'user', '/users/')
app.register_view(TemplateView, 'template', '/templates/')
app.register_view(MessageView, 'message', '/users/<username>/messages/')


print app.url_map

if __name__ == '__main__':
    __package__ = 'restful'
    app.run(debug=True)
