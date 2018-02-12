from hopeit.actions.calculate_dashboard import CalculateDashboardAction
from hopeit.api.resources import CallAction, Resource


class Item(Resource):
    on_get = CallAction(CalculateDashboardAction)
