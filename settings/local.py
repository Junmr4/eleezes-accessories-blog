from settings.base import *
  



DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blogdb',
        'USER': 'june',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
