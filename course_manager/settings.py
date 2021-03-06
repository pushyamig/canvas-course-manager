"""
Django settings for canvas_course_manager project.

Generated by 'django-admin startproject' using Django 2.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPLICATION_DIR = os.path.dirname(globals()['__file__'])
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), ".."),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.ngrok.io']

# Application definition

INSTALLED_APPS = [
    'course_manager',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django_lti_auth',
    'webpack_loader',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'course_manager.urls'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(APPLICATION_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'course_manager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.getenv('MYSQL_ENGINE','django.db.backends.mysql'),
        'NAME': os.getenv('MYSQL_DATABASE', 'course_manager'),
        'USER': os.getenv('MYSQL_USER', 'user'),
        'PASSWORD': os.getenv('MYSQL_PASSWORD', 'password'),
        'HOST': os.getenv('MYSQL_HOST', 'localhost'),
        'PORT': os.getenv('MYSQL_PORT', 3306),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = os.getenv("TZ", "America/Detroit")

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
NPM_ROOT_PATH = BASE_DIR
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)
WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
    }
}

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)


PYLTI_CONFIG = {
    "consumers": {"key": {"secret": "secret"}},
    "method_hooks":{
        "valid_lti_request": "course_manager.lti.valid_lti_request",
        "invalid_lti_request": "course_manager.lti.invalid_lti_request"
    },
    "next_url": "home"
}
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'npm.finders.NpmFinder',
)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # Gunicorns logging format https://github.com/benoitc/gunicorn/blob/19.x/gunicorn/glogging.py
    'formatters': {
        "generic": {
            "format": "%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s",
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
            "class": "logging.Formatter",
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'generic',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'INFO',
        },
        '': {
            'level': 'WARNING',
            'handlers': ['console'],
        },

    },
    'root': {
        'level': 'INFO',
        'handlers': ['console']
    },
}
# print(PYLTI_CONFIG)
# CSP = {
#     "REPORT_ONLY": True,
#     "DEFAULT_SRC": ["'self'","example.edu"],
#     "SCRIPT_SRC": ["'self'", "'unsafe-inline'", "'unsafe-eval'", "www.google-analytics.com"],
#     "IMG_SRC": ["'self'", "data:", "www.google-analytics.com"],
#     "OBJECT_SRC": [],
#     "MEDIA_SRC": [],
#     "FRAME_SRC": ["instructure.com"],
#     "FONT_SRC": ["'self'", "fonts.gstatic.com"],
#     "CONNECT_SRC": [],
#     "STYLE_SRC": ["'self'", "'unsafe-inline'"],
#     "BASE_URI": [],
#     "FRAME_ANCESTORS": [],
#     "FORM_ACTION": [],
#     "SANDBOX": [],
#     "REPORT_URI": [],
#     "MANIFEST_SRC": [],
#     "WORKER_SRC": [],
#     "PLUGIN_TYPES": [],
#     "REQUIRE_SRI_FOR": [],
#     "UPGRADE_INSECURE_REQUESTS": False,
#     "BLOCK_ALL_MIXED_CONTENT": False,
#     "INCLUDE_NONCE_IN": []
# }
# for csp_key, csp_val in CSP.items():
#     globals()["CSP_"+csp_key] = csp_val

# MIDDLEWARE += ['csp.middleware.CSPMiddleware',]
CANVAS_INSTANCE = os.getenv('CANVAS_INSTANCE')
CANVAS_ROOT_ACCOUNT_ID = os.getenv('CANVAS_ROOT_ACCOUNT_ID')
CANVAS_API_TOKEN = os.getenv('CANVAS_API_TOKEN')

CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS=f'ALLOW-FROM {CANVAS_INSTANCE}'
if CSRF_COOKIE_SECURE:
    CSRF_TRUSTED_ORIGINS = ["instructure.com"]
    SESSION_COOKIE_SECURE = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SAMESITE = None
CSRF_COOKIE_SAMESITE = None
