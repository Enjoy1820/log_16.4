"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 4.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import logging
logger = logging.getLogger('django')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j#=)hma&gz*-r-yl!l&8ch=8l%6t48$5m$fnpf2w-i(jz-l4id'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',



    'news',
    'accounts',
    'django_filters',
    'sign',
    'protect',
    'appointments',
    'django_apscheduler',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',

]

ROOT_URLCONF = 'NewsPortal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',
]


WSGI_APPLICATION = 'NewsPortal.wsgi.application'

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}



CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'



EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'Enjoy8487'
EMAIL_HOST_PASSWORD = 'qwqksosongxjiseb'  # пароль от почты
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = 'Enjoy8487@yandex.ru'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ADMINS = [
    ('Владелец зоопарка', 'Enjoy8487@yandex.ru'),
    # список всех админов в формате ('имя', 'их почта')
]
SERVER_EMAIL = 'Enjoy8487@yandex.ru'  # это будет у нас вместо аргумента FROM в массовой рассылке

MANAGERS = [
    ('Вероника Александровна', 'nikaerofeeva.arch@gmail.com'),
    ('Тот самый человек', 'Vladimirluk2537@bk.ru'),

]

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
        'TIMEOUT': 300,
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style': '{',
    'formatters': {
        'common': {
            'format': '%(asctime)s %(levelname)s %(message)s',
            'datefmt': "%d.%m.%Y %H:%M:%S",
        },
        'common_warning': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s',
            'datefmt': "%d.%m.%Y %H:%M:%S",
        },
        'common_error': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s',
            'datefmt': "%d.%m.%Y %H:%M:%S",
        },
        'general': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s',
            'datefmt': "%d.%m.%Y %H:%M:%S",
        },
        'errors': {
            'format': '%(asctime)s %(levelname)s %(pathname)s %(message)s %(exc_info)s',
            'datefmt': "%d.%m.%Y %H:%M:%S",
        },
        'email': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s',
            'datefmt': "%d.%m.%Y %H:%M:%S",
        },
        'security': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s',
            'datefmt': "%d.%m.%Y %H:%M:%S",
        }
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'common',
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'common_warning',
        },
        'console_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'common_error',
        },
        'general': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': 'logs/general.log',
            'formatter': 'general',
        },
        'errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'logs/errors.log',
            'formatter': 'errors',
        },
        'security': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/security.log',
            'formatter': 'security',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'email',
        },
    },

    'loggers': {
        'django': {
            'handlers': ['console', 'console_warning', 'console_error', 'general'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['errors', 'mail_admins'],
            'propagate': True,
        },
        'django.server': {
            'handlers': ['errors', 'mail_admins'],
            'propagate': True,
        },
        'django.template': {
            'handlers': ['errors'],
            'propagate': True,
        },
        'django.db_backends': {
            'handlers': ['errors'],
            'propagate': True,
        },
        'django.security': {
            'handlers': ['security'],
            'propagate': True,
        }
    },
}