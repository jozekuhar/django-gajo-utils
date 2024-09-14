import dataclasses

from django.conf import settings

DEFAULT_GAJO_UTILS_CONFIG = {
    'REQUEST_TIMER': True,
    'REQUEST_DELAY': True,
    'REQUEST_COOKIES': True,
    'RESPONSE_COOKIES': False,
    'RESPONSE_CONTENT': False,
}

USER_CONFIG = getattr(settings, 'GAJO_UTILS_CONFIG', {})

config = DEFAULT_GAJO_UTILS_CONFIG | USER_CONFIG
