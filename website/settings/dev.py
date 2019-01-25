from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(lgq&f!@il4tw#nbwmc)bhe!g3%v=gn62-ya&!8+^h=_(o+e$8'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + ['django_extensions',]

# Allow any passwords in dev.
AUTH_PASSWORD_VALIDATORS = []

try:
    from .local import *
except ImportError:
    pass
