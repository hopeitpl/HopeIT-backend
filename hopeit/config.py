from chaps import scope, SINGLETON_SCOPE


GOOGLE_API_KEY = 'AIzaSyDhUCSp2rS-zGjaasoyv_0Ona_Z915p7ys'
USERNAME = 'admin'
PASSWORD = 'admin'


@scope(SINGLETON_SCOPE)
class Config:
    DATABASE_URL = 'sqlite:///sql.db'
