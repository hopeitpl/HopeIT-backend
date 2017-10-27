from chaps import scope, SINGLETON_SCOPE


@scope(SINGLETON_SCOPE)
class Config:
    DATABASE_URL = 'sqlite:///sql.db'