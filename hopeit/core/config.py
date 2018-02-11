import os

from chaps import SINGLETON_SCOPE, scope

db = os.environ['DB']


@scope(SINGLETON_SCOPE)
class Config:
    DATABASE_URL = os.environ.get(
        'DATABASE_URL',
        f'postgresql://postgres:postgres@hopeit.karkut.info/{db}')
    PAYMENT_URL = 'https://ssl.dotpay.pl/test_payment/?'
    SHOP_ID = '780663'
    GOOGLE_API_KEY = 'AAAATiFbYrA:APA91bHVApgAlqi3bKBrtmYmyjZjIoRqyJSCFcUcP' \
                     'IIZg5J0_R1yFkaYaR-j0Te5KXyNFmqKmvxfj6tMcEzOuFIiailYjx' \
                     'ExCZrke7FJvhmfg530T5pPRkOElC8EbIg9hd1jZAIsCKl-'
    USERNAME = 'admin'
    PASSWORD = 'admin'
