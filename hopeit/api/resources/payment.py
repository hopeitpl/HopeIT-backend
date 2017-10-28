import json

from chaps import inject

from hopeit.actions.create_payment import CreatePaymentAction
from hopeit.api.resources import CallAction, Resource
from hopeit.models.payment import Payment


class CreatePayment(Resource):
    on_post = CallAction(CreatePaymentAction)


@inject('db_session')
class GetPaymentStatus(Resource):
    def on_post(self, req, _):
        data = json.dumps(str(req.stream.read(), "utf-8")).replace('%40', '@').split('&')
        dict_data = dict(s.split('=') for s in [a.replace('"', '') for a in data])

        payment = Payment(
            operation_number=dict_data['operation_number'],
            operation_type=dict_data['operation_type'],
            operation_status=dict_data['operation_status'],
            operation_amount=dict_data['operation_amount'],
            operation_currency=dict_data['operation_currency'],
            operation_datetime=dict_data['operation_datetime'],
            description=dict_data['description'],
            email=dict_data['email'],
            channel=dict_data['channel'],
            signature=dict_data['signature']
        )
        self.db_session.add(payment)

        return {
            'results': 'OK'
        }
