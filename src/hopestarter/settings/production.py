import raven
from .world import *
from .space import *
from .utils import get_env_variable
from .auth import *

try:
    from .api_secret import *
    RAVEN_CONFIG = {
        'dsn': RAVEN_DSN
    }
    INSTALLED_APPS += ("raven.contrib.django.raven_compat",)
except ImportError:
    pass

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = []

MIDDLEWARE_CLASSES = (
  'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware',
  'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware',
) + MIDDLEWARE_CLASSES


SECRET_KEY = get_env_variable("SECRET_KEY")

SITE_ID = 1

GRAPPELLI_INDEX_DASHBOARD = 'hopestarter.dashboard.CustomIndexDashboard'
