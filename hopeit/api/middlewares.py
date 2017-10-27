import json
import falcon


class SerializationMiddleware(object):
    def process_request(self, req, resp):
        if (req.content_length and req.content_type and
                req.content_type.startswith('application/json')):
            req.payload = json.load(req.stream)
        else:
            req.payload = {}

    def process_response(self, req, resp, resource, req_succeeded):
        try:
            obj = resp.payload
        except AttributeError:
            pass
        else:
            if obj:
                if not isinstance(obj, dict):
                    assert hasattr(obj, 'to_dict'), (
                        'Obj {} has no to_dict method')
                    obj = obj.to_dict()
                resp.body = json.dumps(obj)