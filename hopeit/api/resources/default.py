import json

from hopeit.api.resources import Resource


class Default(Resource):
    def on_get(self, req, resp):
        resp.body = json.dumps({'working': True}, ensure_ascii=False)
