import os

from chaps import SINGLETON_SCOPE, scope


@scope(SINGLETON_SCOPE)
class Config:
    DATABASE_URL = os.environ.get(
        'DATABASE_URL',
        'postgres://postgres:postgres@localhost:5432/postgres')
    PAYMENT_URL = os.environ.get('PAYMENT_URL')
    SHOP_ID = os.environ.get('SHOP_ID')
    GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
    USERNAME = os.environ.get('USERNAME', 'admin')
    PASSWORD = os.environ.get('PASSWORD', 'admin')
