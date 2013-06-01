from restful.odm import Field, Link, Model, Relationship

__all__ = ['Template', 'User', 'Message']


class User(Model):
    """User model."""
    class __mongometa__:
        name = 'users'

    username = Field(str, required=True, unique=True)
    email = Field(str, required=True)
    first_name = Field(str)
    last_name = Field(str)
    is_active = Field(bool, if_missing=True)
    messages = Relationship('Message')


class Message(Model):
    """Message model."""
    class __mongometa__:
        name = 'messages'

    subject = Field(str, required=True)
    plaintext = Field(str)
    html = Field(str)
    user_id = Link('User')
    user = Relationship('User')
    template_id = Link('Template')
    template = Relationship('Template')


class Template(Model):
    """Message template model."""
    class __mongometa__:
        name = 'templates'

    name = Field(str, required=True)
    subject = Field(str)
    plaintext = Field(str)
    html = Field(str)
