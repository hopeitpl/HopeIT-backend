import scopectx
from chaps.scope import Scope

REQUEST_SCOPE = '__request'


class RequestScope(Scope):
    scope = scopectx.Context()

    def get_object(self, class_):
        try:
            objects = self.scope['objects']
        except KeyError:
            objects = {}
            self.scope['objects'] = objects

        if class_ in objects:
            return objects[class_]
        else:
            obj = class_()
            objects[class_] = obj
            return obj