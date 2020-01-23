import os
from .settings import *

DEBUG = False
ALLOWED_HOSTS = [os.getenv('SITE_HOST')]
COMPRESS_OFFLINE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': 5432
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'NOTSET',
        'handlers': ['file']
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'formatter': 'detailed',
            'filename': '/var/log/portfolio/portfolio.log',
            'mode': 'a',
            'maxBytes': 10485760,
            'backupCount': 5
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        },
    },
    'formatters': {
        'detailed': {
            'format': '%(asctime)-s %(module)-17s line:%(lineno)-4d %(levelname)-s %(message)s',
        }
    }
}
