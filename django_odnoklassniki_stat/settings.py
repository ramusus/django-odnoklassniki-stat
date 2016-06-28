"""
Django settings for untitled1 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ymo4)pz15_yl5q@9&is(7q60ang!57a3zc5e2m8lp8hb1dd_k&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'odnoklassniki_stats',
    'oauth_tokens',
    'taggit',
    'odnoklassniki_api',
    'odnoklassniki_groups',
    'm2m_history',
    'odnoklassniki_users',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'social_auth.backends.contrib.odnoklassniki.OdnoklassnikiBackend',
)

ROOT_URLCONF = 'django_odnoklassniki_stat.urls'

WSGI_APPLICATION = 'django_odnoklassniki_stat.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'stat',
            'USER': 'postgres',
            'PASSWORD': 877,
            'HOST': 'localhost',
            'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (os.path.join(BASE_DIR,  'templates'),)

SOCIAL_API_CALL_CONTEXT = {
    'odnoklassniki': {'token' : 'tkn18ZDxQAyoqpLpSXpnEbcep4ggbImu0E14Z8riEJv3wutOPy23dAX3lgCMnTAe7HIR9'
                      },
}

OAUTH_TOKENS_ODNOKLASSNIKI_CLIENT_ID = 1085608704
OAUTH_TOKENS_ODNOKLASSNIKI_CLIENT_PUBLIC = 'CBAEBGLBEBABABABA'
OAUTH_TOKENS_ODNOKLASSNIKI_CLIENT_SECRET = '1CEF9916FCDF50C873D231B3'
OAUTH_TOKENS_ODNOKLASSNIKI_SCOPE = ['VALUABLE_ACCESS', 'VIDEO_CONTENT', 'GROUP_CONTENT']
OAUTH_TOKENS_ODNOKLASSNIKI_USERNAME = 'baranus@mail.ru'
OAUTH_TOKENS_ODNOKLASSNIKI_PASSWORD = 's0cial'
