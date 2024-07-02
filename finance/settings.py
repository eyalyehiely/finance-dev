"""
Django settings for finance project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta
from redis import Redis
from dotenv import load_dotenv
from datetime import timedelta
from django.conf import global_settings
import certifi

load_dotenv()
SITE_ID =1
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)s+d6bs$ft@m#vdgt#jba0qy9sgumx&__=l&q0p3@&^mj%+$m('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG',False)

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS',['*'])

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'backend',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    'drf_yasg',
    'corsheaders',
    'users',
    'django.contrib.sites',
    'debug_toolbar',
    'rest_framework_simplejwt.token_blacklist',


]



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',

    ]
}




SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),  # Token expiration time
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),     # Refresh token expiration time
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,
    
    'ALGORITHM': 'HS256',  # Token encryption algorithm
    'VERIFYING_KEY': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',
    
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}


SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Basic': {
            'type': 'basic'
        }
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


ROOT_URLCONF = 'finance.urls'

CORS_ALLOWED_ORIGINS = [
    os.environ.get('FRONTEND_URL','http://localhost:5173'),
    # Add other origins as needed
]
CORS_ORIGIN_ALLOW_ALL = True

# CSRF_TRUSTED_ORIGINS = ['http://localhost:5173']



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'frontend/src')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request'
            ],
        },
    },
]





WSGI_APPLICATION = 'finance.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME','railway'),
        'USER': os.environ.get('DATABASE_USER','postgres'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD','nSObSkPFOFpFqWrDPUlsHroWLCGJInhu'),
        'HOST': os.environ.get('DATABASE_HOST','viaduct.proxy.rlwy.net'),
        'PORT': os.environ.get('DATABASE_PORT','25017'),                   
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }




# Password validation
AUTH_USER_MODEL = 'users.CustomUser'

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Jerusalem'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'eyalwork0@gmail.com'
EMAIL_HOST_PASSWORD = 'kanw zgwa xeot cxfx'
DEFAULT_FROM_EMAIL = 'eyalwork0@gmail.com'




os.environ['SSL_CERT_FILE'] = certifi.where()



# social authentication
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]


# logs
LOGGING = {
    'version': 1,
    'loggers': {
        'backend': {
            'handlers': ['backend_file'],
            'level': 'DEBUG',
        },
        'users': {
            'handlers': ['users_file'],
            'level': 'DEBUG',
        }
    },
    'handlers': {
        'backend_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': './logs/backend.log',
            'formatter': 'simpleRe',
        },
        'users_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': './logs/users.log',
            'formatter': 'simpleRe',
        },
        'example_file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': './logs/debug3.log',
            'formatter': 'simpleRe',
        }
    },
    'formatters': {
        'simpleRe': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        }
    }
}


CORS_ALLOW_ALL_ORIGIN = True
