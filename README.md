# Kosmolog

## Technologies used
 - [Falcon](https://falconframework.org/)
 - [SQLAlchemy](http://docs.sqlalchemy.org/en/latest/)
 - [Marshmallow](https://marshmallow.readthedocs.io/en/latest/)

## Requirements
 - Python 3.6+

## Installation

1. Install requirements
 - `pip install -r requirements.dev.txt`
2. Install hopeit module
 - `python setup.py develop`
2. Setup PosgreSQL database. Database url can be configured by [DATABASE_URL](/hopeit/core/config.py) env var.
3. Run migrations
 - `alembic upgrade head`
4. Start UWSGI
 - `uwsgi uwsgi.ini`
5. Go to `localhost:8000` and see if it is working.
