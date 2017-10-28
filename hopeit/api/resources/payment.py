import json

from hopeit.actions.create_payment import CreatePaymentAction
from hopeit.api.resources import CallAction, Resource


class CreatePayment(Resource):
    on_post = CallAction(CreatePaymentAction)


class GetPaymentStatus:
    def on_post(self, req, _):
        data = json.dumps(str(req.stream.read(), "utf-8")).replace('%40', '@').split('&')
        dict_data = dict(s.split('=') for s in [a.replace('"', '') for a in data])

        # TODO: Save data to Payment model

        return {
            'results': 'OK'
        }
