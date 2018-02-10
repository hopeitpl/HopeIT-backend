from chaps import Inject


class Dotpay:
    config = Inject('config')

    def __init__(self):
        self.payment_url = self.config.PAYMENT_URL

    def get_payment_data(self, amount, description):
        return {
            'id': self.config.SHOP_ID,
            'amount': amount,
            'description': description
        }

    def build_payment_url(self, payment):
        params = "&".join(
            ["=".join([key, str(val)]) for key, val in payment.items()])
        return self.payment_url + params
