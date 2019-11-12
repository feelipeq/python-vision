import os
from . import constants

PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXTENSIONS=['*.jpg','*.jpeg','*.png']
FOLDER='161pryZMzKGWawRZ2wV5qStfuK0R_OIcq'
LANG="pt-br"
SECRET="C:/Users/Felip/Downloads/Quickstart-09f65f8f8289.json"


SIMPLE_SETTINGS = {
    'CONFIGURE_LOGGING': True
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(name)s %(module)s %(process)d %(thread)d %(message)s'  # noqa
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(name)s %(message)s'  # noqa
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'level': 'INFO',
            'filters': []
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, '..', '..', 'imagesvision.log'),
            'maxBytes': 10 * constants.MEGA_BYTES,
            'backupCount': 2,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'bettercall': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'asyncio': {
            'level': 'WARNING',
            'propagate': True,
        },
    }
}
