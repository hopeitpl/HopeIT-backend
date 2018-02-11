from hopeit.actions.update_user_device import UpdateUserDeviceAction
from hopeit.api.resources import CallAction, Resource


class Item(Resource):
    on_post = CallAction(UpdateUserDeviceAction)
