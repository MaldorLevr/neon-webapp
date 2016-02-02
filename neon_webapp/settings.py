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


if os.environ.get('SECRET_KEY'):
    # if in production
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.environ['SECRET_KEY']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'django',
            'USER': 'django',
            'PASSWORD': 'kKzvQCcBBJ',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
    DEBUG = True

    STATIC_ROOT = '/home/django/static/'

    ALLOWED_HOSTS = [
        '127.0.0.1',
        u'127.0.0.1',
        '107.170.252.240',
        'windsorapp.me',
        '.windsorapp.me',
        'windsorapp.me.',
    ]
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
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'neon_postgres',
            'USER': 'postgres',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
