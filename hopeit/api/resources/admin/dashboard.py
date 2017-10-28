from hopeit.actions.calculate_dashboard import CalculateDashboardAction
from hopeit.api.resources import Resource, CallAction


class Item(Resource):
    on_get = CallAction(CalculateDashboardAction)
