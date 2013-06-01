import decimal

from bson import ObjectId
from flask import (current_app, got_request_exception, json, request,
                   request_finished, request_started, template_rendered)

__all__ = ['jsonify', 'subscribe_logging_helpers']


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, '__json__') and callable(obj.__json__):
            return obj.__json__()
        # encode date and datetime objects using ISO format
        elif hasattr(obj, 'isoformat') and callable(obj.isoformat):
            return obj.isoformat()
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        elif isinstance(obj, ObjectId):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)


def jsonify(*args, **kwargs):
    return json.dumps(dict(*args, **kwargs), default=JSONEncoder().default,
                      indent=4 if current_app.debug else None)


def subscribe_logging_helpers(app):
    """
    Configure functions that log in response to Flask signals emitted by app.

    Flask signal            function invoked
    ------------            -------------------
    request_started         log_request
    template_rendered       log_template_rendered
    request_finished        log_response
    got_request_exception   log_exception

    """
    request_started.connect(log_request, app)
    template_rendered.connect(log_template_rendered, app)
    request_finished.connect(log_response, app)
    got_request_exception.connect(log_exception, app)


def log_template_rendered(sender, template, context, **extra):
    """Log that the sender rendered a template."""
    sender.logger.debug('Rendering template "%s" with context %s',
                        template.name or 'string template', context)


def log_request(sender, **extra):
    """Log that the sender began processing a request."""
    sender.logger.debug('Request context is set up.' 'Request: %s', request)


def log_response(sender, response, **extra):
    """Log that the sender finished processing a request."""
    sender.logger.debug('Request context is about to close down. Response: %s',
                        response)


def log_exception(sender, exception, **extra):
    """Log that sender encountered an exception while processing a request."""
    sender.logger.error('Exception ocurred during processing: %s', exception)
