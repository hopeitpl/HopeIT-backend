import os
from chaps import scope, SINGLETON_SCOPE

db = os.environ['DB']

@scope(SINGLETON_SCOPE)
class Config:
    DATABASE_URL = f'postgresql://postgres:postgres@hopeit.karkut.info/{db}'
    PAYMENT_URL = 'https://ssl.dotpay.pl/test_payment/?'
    SHOP_ID = '780663'
    GOOGLE_API_KEY = 'AIzaSyDhUCSp2rS-zGjaasoyv_0Ona_Z915p7ys'
    USERNAME = 'admin'
    PASSWORD = 'admin'
