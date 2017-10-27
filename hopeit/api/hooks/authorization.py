import base64

import falcon
from chaps import Inject

TOKEN_REQUIRED = 'Please provide authorization token'
TOKEN_INVALID = 'Please provide proper authorization token'
TOKEN_INVALID_CREDENTIALS = 'Please provide proper credentials.'


class Authorization(object):
    config = Inject('config')

    def __call__(self, req, resp, **kwargs):
        token = req.get_header('Authorization')

        if token is None:
            raise falcon.HTTPUnauthorized(description=TOKEN_REQUIRED)

        if 'Basic' not in token:
            raise falcon.HTTPUnauthorized(description=TOKEN_INVALID)
        _, token = token.split()

        try:
            user = base64.b64decode(token).decode('utf-8')
        except base64.binascii.Error:
            raise falcon.HTTPUnauthorized(description=TOKEN_INVALID)

        if user != f'{self.config.USERNAME}:{self.config.PASSWORD}':
            raise falcon.HTTPUnauthorized(
                description=TOKEN_INVALID_CREDENTIALS)


def authorize_user(func):
    action = Authorization()

    def _inner(self, req, resp, **kwargs):
        action(req, resp, **kwargs)
        return func(req, resp, **kwargs)

    return _inner
