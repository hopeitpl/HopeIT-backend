from chaps import Inject


class Action:
    app = Inject('app')

    def __init__(self, **data):
        self.__dict__.update(data)

    def do(self):
        raise NotImplementedError
