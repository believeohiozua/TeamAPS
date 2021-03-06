"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = '587'
EMAIL_USE_TLS = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y5t&4pi^d&mwj=w6ycvnsxiodp9yiwgp0j!cnhi+(%r^^axf$='

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
	'profiles',
	'contact',
	'crispy_forms',
	'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
	'catalog.apps.CatalogConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

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

AUTHENTICATION_BACKENDS = (
   
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)



WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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
"""
if DEBUG:
	MEDIA_URL = '/media/'
	STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static-only")
	MEDIA_ROOT =  os.path.join(os.path.dirname(BASE_DIR), "static", "media")
	STATICFILES_DIRS = (os.path.join(os.path.dirname(BASE_DIR), "static", "static"),)
"""
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static-only")
MEDIA_ROOT =  os.path.join(os.path.dirname(BASE_DIR), "static", "media", 'static/img/uploads')
STATICFILES_DIRS = (os.path.join(os.path.dirname(BASE_DIR), "static", "static"),)


CRISPY_TEMPLATE_PACK = 'bootstrap3'

SITE_ID = 1

LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/'

ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACOUNT_CONFIRM_EMAIL_ON_GET = False
ACOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL
ACOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None

ACOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACOUNT_EMAIL_REQUIRED = True
ACOUNT_EMAIL_VERIFIATION = None
ACOUNT_EMAIL_SUBJECT_PREFIX = "my subject: "
ACOUNT_DEFAULT_HTTP_PROTOCOL = "http"

ACOUNT_LOGOUT_ON_GET = False
ACOUNT_LOGOUT_REDIRECT_URL = "/"
ACOUNT_SIGNUP_FORM_CLASS = None
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True
ACCOUNT_UNIQUE_EMAIL = True
ACOUNT_USER_MODEL_USERNAME_FIELD = "username"
ACOUNT_USER_MODEL_EMAIL_FIELD = "email"

ACOUNT_USERNAME_MIN_LENGTH = 5
ACOUNT_USERNAME_BLACKLIST = []
ACOUNT_USERNAME_REQUIRED = True
ACOUNT_PASSWORD_INPUT_RENDER_VALUE = False
ACOUNT_PASSWORD_MIN_LENGTH = 6
ACOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
