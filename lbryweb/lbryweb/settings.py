"""
Django settings for lbryweb project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z5xvlhbnkfwccng@2kdl^yx!5^18ah(leh2%s_nv^jdnoc3ao@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',

    'users.apps.UsersConfig',
    'registration.apps.RegistrationConfig',
    'storage.apps.StorageConfig',
    'main.apps.MainConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'main.middleware.LbrynetAccountMiddleware',
    'main.middleware.AccountIdCookieMiddleware'
]

ROOT_URLCONF = 'lbryweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'lbryweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_NAME', 'lbryweb_prototype'),
        'USER': os.getenv('POSTGRES_USER', 'lbryweb'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', ')UiCMCiWRcee9Yg'),
        'HOST': os.getenv('POSTGRES_HOST', '127.0.0.1'),
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

AUTH_USER_MODEL = 'users.User'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'WARNING'
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'  # noqa
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'timber': {
            'level': 'DEBUG',
            'class': 'timber.TimberHandler',
            'formatter': 'simple',
            'api_key': '6515_9a5e7c6c749b569e:187934f2a0c1a8f2ec7674d079874b81744a1d8e8650103379d7d1a7751f8d11',
            'raise_exceptions': True
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'daemon.api': {
            'handlers': ['timber'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'storage.views': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        }
    },
}

STATIC_ROOT = os.path.join(BASE_DIR, '../static/')

if 'test' in ' '.join(sys.argv):
    del LOGGING['handlers']['timber']
else:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn="https://4cec5c27f13a4205842306a8415e7f45@sentry.io/1324446",
        integrations=[DjangoIntegration()]
    )

# Default: for running code on your host machine and access daemon_test_local container from docker-compose
LBRY_DAEMON = os.getenv('LBRY_DAEMON', 'http://localhost:5479/')
# Default: shared dir for daemon_test_local
LBRY_DOWNLOAD_DIRECTORY = os.getenv(
    'LBRY_DOWNLOAD_DIRECTORY',
    os.path.join(BASE_DIR, '../.daemon_test_local_storage/download')
)
LBRY_CONTENT_URL = os.getenv('LBRY_CONTENT_URL', 'http://localhost:8000/storage/content/')
