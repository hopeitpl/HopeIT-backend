import base64
import falcon
from chaps import inject


from hopeit.config import USERNAME, PASSWORD

TOKEN_REQUIRED = 'Please provide authorization token'
TOKEN_INVALID = 'Please provide proper authorization token'
TOKEN_INVALID_CREDENTIALS = 'Please provide proper credentials.'


class Authorization(object):

    @inject
    def __init__(self):
        pass

    def __call__(self, req, resp, resource, params):
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

        if user != f'{USERNAME}:{PASSWORD}':
            raise falcon.HTTPUnauthorized(
                description=TOKEN_INVALID_CREDENTIALS)


def authorize_user(req, resp, resource, params):
    return Authorization()(req, resp, resource, params)
