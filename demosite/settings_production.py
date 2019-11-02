import os
from demosite.settings import *

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

SECRET_KEY = ',O@e{DQ739-DrO~S@l0.7)T+T]3buZ%&Yt./H#HSl<lzd9qSc~_Fqwksp$KgGg^'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'demo',
            'USER': 'demo'
    }
}
