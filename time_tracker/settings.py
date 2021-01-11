from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#ln=jyy$poq!9xpb834%h*a+wup(=l@k+iis*cnn^za#=ne92j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['yousefhou.pythonanywhere.com']

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'TimeTracker',
]

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_AUTHENTICATION_METHOD = "email"

ACCOUNT_FORMS = {'signup': 'TimeTracker.forms.MyCustomSignupForm'}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'time_tracker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates", ""
            "time_tracker/templates/",
            os.path.normpath(os.path.join(BASE_DIR, 'templates')),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
            os.path.join(os.path.dirname(__file__), 'templates').replace('\\', '/')
                 ],
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

WSGI_APPLICATION = 'time_tracker.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    #{
    #    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    #},
    #{
    #    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    #},
    #{
    #    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    #},
    #{
    #    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    #},
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "../static"),

)

STATIC_URL = '/static/'


TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'templates/'),
]

# BOOTSTRAP4 = {
#     'include_jquery': True,
# }
FORMAT_MODULE_PATH = 'demo_time_set.formats'
