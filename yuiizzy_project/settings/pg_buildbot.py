from yuiizzy_project.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'yuiizzy',
        'USER': 'yuiizzyuser',
        'PASSWORD': 'yuiizzypass',
        'HOST': '',
        'PORT': '',
    }
}
