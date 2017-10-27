from typing import Type

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
        return {'payload': payload}

    def __call__(self, req, resp, **kwargs):
        resp.payload = self.app.run(
            self.action(self.validate(req, kwargs)))


class Resource:
    app = Inject('app')
