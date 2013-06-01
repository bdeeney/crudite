from crudite.views import CruddyMingView

from restful.model import User, Template, Message


class UserView(CruddyMingView):
    model = User
    pk = 'username'
    pk_type = 'string'


class TemplateView(CruddyMingView):
    model = Template

    __methods__ = ['GET']


class MessageView(CruddyMingView):
    model = Message

    def index(self, username, **kwargs):
        user = User.query.find({'username': username}).first()
        return super(MessageView, self).index(user_id=user._id)
