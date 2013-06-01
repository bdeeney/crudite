from flask.wrappers import (Request as BaseRequest,
                            Response as BaseResponse)

__all__ = ['Request', 'Response']


class Request(BaseRequest):
    """Base class for Crudite Request classes."""

    is_json = property(lambda x: x.mimetype == 'application/json', doc='''
            True if the request's mimetype is 'application/json'.''')


class Response(BaseResponse):
    pass
