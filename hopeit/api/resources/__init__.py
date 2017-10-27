from typing import Type

import falcon
from chaps import Inject

from hopeit.actions import Action


class CallAction:
    app = Inject('app')

    def __init__(self, action: Type[Action], validator=None):
        self.action = action
        self.validator = validator

    def validate(self, req, extra):
        payload = req.payload
        if payload is not None:
            payload = req.payload.copy()
            payload.update(extra)
        else:
            payload = extra

        if self.validator is not None:
            schema = self.validator()
            data = payload.copy()
            result = schema.load(data)

            if result.errors:
                raise falcon.HTTPBadRequest(
                    'Validation Error',
                    result.errors
                )
            else:
                payload = result.data

        return {'payload': payload}

    def __call__(self, req, resp, **kwargs):
        resp.payload = self.app.run(
            self.action(self.validate(req, kwargs)))


class Resource:
    app = Inject('app')
