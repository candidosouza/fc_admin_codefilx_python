"""
Django settings for django_app project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# DDD / mudar a raiz do projeto com o BASE_DIR, adicionar mais um .parent
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-snc114g(q@fjv^y209u&r5(3qfp0n9y2hht+fm_(-y$hqsl5w)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # elasticapm
    'elasticapm.contrib.django',
    'django_prometheus',
    'django_extensions',
    'core.category.infra.django'
]

MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',
    'elasticapm.contrib.django.middleware.TracingMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_prometheus.middleware.PrometheusAfterMiddleware',
]

ELASTIC_APM = {
    # Set required service name. Allowed characters:
    # a-z, A-Z, 0-9, -, _, and space
    'SERVICE_NAME': 'fcadminpython',

    # Set custom APM Server URL (default: http://localhost:8200)
    'SERVER_URL': 'http://apm:8200',
    'DEBUG': True,
    'ENVIRONMENT': 'production',
}

ROOT_URLCONF = 'django_app.urls'

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
                'elasticapm.contrib.django.context_processors.rum_tracing',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        # prometheus monitoring your databases
        'ENGINE': 'django_prometheus.db.backends.sqlite3',
        # 'ENGINE': 'django.db.backends.sqlite3',
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

# prometheus monitoring your caches
CACHES = {
    'default': {
        'BACKEND': 'django_prometheus.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}

# prometheus configuration
PROMETHEUS_LATENCY_BUCKETS = (0.01, 0.025, 0.05, 0.075, 0.1, 0.25, 0.5,
                              0.75, 1.0, 2.5, 5.0, 7.5, 10.0, 25.0, 50.0, 75.0, float("inf"),)
PROMETHEUS_LATENCY_BUCKETS = (.1, .2, .5, .6, .8, 1.0, 2.0, 3.0,
                              4.0, 5.0, 6.0, 7.5, 9.0, 12.0, 15.0, 20.0, 30.0, float("inf"))
# prometheus "/prometheus/metrics"
# ROOT_URLCONF = "django_app.urls_prometheus_wrapper"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'elasticapm': {
            'level': 'WARNING',
            'class': 'elasticapm.contrib.django.handlers.LoggingHandler',
            # 'filename': Path(BASE_DIR).resolve().joinpath('logs', 'app.log'),
            # 'maxBytes': 1024 * 1024 * 15,  # 15MB
            # 'backupCount': 10,
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['elasticapm'],
            'propagate': True,
        },
        'mysite': {
            'level': 'WARNING',
            'handlers': ['elasticapm'],
            'propagate': True,
        },
        # Log errors from the Elastic APM module to the console (recommended)
        'elasticapm.errors': {
            'level': 'ERROR',
            'handlers': ['elasticapm'],
            'propagate': True,
        },
    },
}

# opentelemetry
DJANGO_SETTINGS_MODULE = 'django_app.settings'
OPENTELEMETRY_DJANGO_INSTRUMENT = True
# OPENTELEMETRY_DJANGO_TRACER_PROVIDER = 'opentelemetry.sdk.trace.TracerProvider'
# OPENTELEMETRY_DJANGO_SPAN_PROCESSORS = [
#     'opentelemetry.sdk.trace.export.SimpleSpanProcessor',
#     'opentelemetry.sdk.trace.export.BatchSpanProcessor',
# ]
# OPENTELEMETRY_DJANGO_EXPORTER = 'opentelemetry.sdk.trace.export.ConsoleSpanExporter'
# OPENTELEMETRY_DJANGO_EXPORTER_ARGS = {
#     'out': sys.stdout,
# }
# OPENTELEMETRY_DJANGO_PROPAGATORS = [
#     'opentelemetry.trace.propagation.tracecontext_http_header_format.TraceContextPropagator',
#     'opentelemetry.trace.propagation.b3_format.B3FormatPropagator',
#     'opentelemetry.trace.propagation.skeleton_format.SkeletonFormatPropagator',
# ]
# OPENTELEMETRY_DJANGO_TRACER_PROVIDER_ARGS = {
#     'active_span_processor': 'opentelemetry.sdk.trace.export.SimpleSpanProcessor',
#     'active_exporter': 'opentelemetry.sdk.trace.export.ConsoleSpanExporter',
#     'active_exporter_args': {
#         'out': sys.stdout,
#     },
#     'active_propagators': [
#         'opentelemetry.trace.propagation.tracecontext_http_header_format.TraceContextPropagator',
#         'opentelemetry.trace.propagation.b3_format.B3FormatPropagator',
#         'opentelemetry.trace.propagation.skeleton_format.SkeletonFormatPropagator',
#     ],
# }
