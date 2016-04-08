import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

REGISTRATION_OPEN = False

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = (
    'Cache-Control',
    'Accept-Encoding',
)

INSTALLED_APPS = (
    'corsheaders',
    'rest_framework',
    'neon_app',
    'huey.contrib.djhuey',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticatedOrReadOnly',)
}

ROOT_URLCONF = 'neon_webapp.urls'

WSGI_APPLICATION = 'neon_webapp.wsgi.application'

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

HUEY = {
    'name': 'my-app',

    # Options to pass into the consumer when running ``manage.py run_huey``
    'consumer': {'workers': 4, 'worker_type': 'thread'},
}

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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = '../static/'


if os.environ.get('SECRET_KEY'):
    # if in production
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.environ['SECRET_KEY']
    PASSWORD = os.environ['DB_PASSWORD']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'django',
            'USER': 'django',
            'PASSWORD': PASSWORD,
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }
    DEBUG = False

    ALLOWED_HOSTS = ['127.0.0.1',
                     u'127.0.0.1',
                     '107.170.252.240',
                     'windsorapp.me', ]

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': '/root/django/debug.log',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
    }

else:
    SECRET_KEY = 'v$n#racg8iqp4d*s+3k@cc^svw7qln@z6%ercj+iw$ub+@a#ma'
    DEBUG = True

    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #     }
    # }

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'django',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }
