import os

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from own_selection_top_films.settings import DEBUG, BASE_DIR


if DEBUG:
    filename = os.path.join(BASE_DIR, 'main.log')
else:
    filename = '/var/log/my_top_movie/main.log'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': filename,
        },
    },
    'loggers': {
        'authentication': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}


sentry_sdk.init(
    dsn="", # Add link for logging
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True
)
