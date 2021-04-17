"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^s=mp8t1-z)rj#b9rk+4him(0i#0g*@^kc@tkdze78kni$+zxx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DEFAULT_FROM_EMAIL = "yuktibajaj85@yahoo.com"
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_EMAIL_VERIFICATION = "none"
try:
    from .email_settings import host, user, password
    EMAIL_HOST = host #"smtp.gmail.com" #"smtp.sendgrid.net"
    EMAIL_HOST_USER = user #"codingforentrepreneurs@gmail.com"
    EMAIL_HOST_PASSWORD = password #"password"
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
except:
    pass

if DEBUG:
    SITE_URL = "http://127.0.0.1:8000"



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products',
    'carts',
    'orders',
    'accounts.apps.AccountsConfig',
    'localflavor',
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

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
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

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_TAX_RATE = 0.08

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR) ,"static", "media")
# MEDIA_ROOT= 'D:/YUKTI Work/PROJECTS/MinorProject/static/media'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR) ,"static", "static_root")

STATICFILES_DIRS = (
                    os.path.join(os.path.dirname(BASE_DIR) ,"static", "static_files"),
)



STRIPE_SECRET_KEY = "sk_test_51IUDLBH5aUhTHSp7AQUkPTL0xxwZdqvCdluGfkxlf0NwxTtIqjiGN2HXoJpe0Rm1yismpnoz5kqL1r4IV3PFFD7s00uY0UMcXv"
STRIPE_PUBLISHABLE_KEY = "pk_test_51IUDLBH5aUhTHSp7bM8cQlzh8Pmbd94Ep7xh74DJxiwIY1eZtPlVGvk0uCy6FnLBYJZI6xa16lDu8lsBHYbP6TvE00bHvfS2CD"
