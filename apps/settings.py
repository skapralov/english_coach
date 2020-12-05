from datetime import timedelta
from os import environ

JWT_ACCESS_LIFETIME = timedelta(minutes=30)
JWT_REFRESH_LIFETIME = timedelta(days=1)
JWT_ALGORITHM = 'HS256'

SECRET = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'

POSTGRES_DB = environ.get('PG_NAME', 'english_coach_db')
POSTGRES_HOST = environ.get('PG_HOST', '127.0.0.1')
POSTGRES_PORT = environ.get('PG_PORT', '5432')
POSTGRES_USER = environ.get('PG_USER', 'english_coach_user')
POSTGRES_PASSWORD = environ.get('PG_PASS', 'fJConT0hgZ')
DATABASE_URI = f'postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

APPS = {
    'aerich': ['aerich.models', ],

    'users': ['apps.users.models', ],
    'words': ['apps.words.models', ],
}

TORTOISE_ORM = {
    'connections': {'default': DATABASE_URI},
    'apps': {app: {'models': models} for app, models in APPS.items()},
}
