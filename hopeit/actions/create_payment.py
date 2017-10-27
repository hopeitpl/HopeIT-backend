import chaps

from hopeit.actions import Action


class CreatePaymentAction(Action):
    def do(self):
        payment = chaps.Container().get_object('payments')
        data = payment.get_payment_data(
            amount=self.payload['amount'],
            description=self.payload['description']
        )

        return {
            'results': payment.build_payment_url(data)
        }
