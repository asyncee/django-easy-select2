"""
Settings for sampleproject project.
"""

import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'CHANGE_IT_FOR_MORE_SECURITY'

INSTALLED_APPS = (
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third-party apps
    'easy_select2',

    # project apps
    'demoapp',
)

MIDDLEWARE = (
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sampleproject.urls'

WSGI_APPLICATION = 'sampleproject.wsgi.application'

#LANGUAGE_CODE = 'ru-RU'

#TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

#FIRST_DAY_OF_WEEK = 1

USE_TZ = False

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
        },
    },
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    ('css', os.path.join(STATIC_ROOT, 'css')),
    ('js', os.path.join(STATIC_ROOT, 'js')),
    ('img', os.path.join(STATIC_ROOT, 'img')),
)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CSRF_COOKIE_NAME = '__csrf'

LANGUAGE_COOKIE_NAME = '__lang'

SESSION_COOKIE_NAME = '__sid'

USE_ETAGS = False

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'auth_login'
LOGOUT_URL = 'auth_logout'

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'file_error_log': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'error.log'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'file_error_log'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

from .local_settings import *