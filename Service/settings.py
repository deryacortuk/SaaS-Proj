from pathlib import Path
import os
import dotenv

env_file = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), '.env')

dotenv.load_dotenv(env_file)

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = "django-insecure-7^+8-$b0_qx&j8@2%0@va7r&ys2b8_i6#g*^z=n)!83uz=*32#"


DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Account.apps.AccountConfig",
    'crispy_forms',
    "crispy_bootstrap5",
    "UserHub.apps.UserhubConfig",
    
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "Service.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR,"templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "Service.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = os.path.join(BASE_DIR,"staticfiles")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,"static"),
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTHENTCATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "Account.authentication.EmailAuthBackend",
]

EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST="smtp.zoho.eu"
EMAIL_USE_SSL = False
EMAIL_PORT = 587
EMAIL_USE_TLS=True
EMAIL_HOST_PASSWORD= os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_HOST_USER= os.environ.get("EMAIL_HOST_USER")


DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

CELERY_BROKER_URL ="redis://localhost:6379/0" 
CELERY_RESULT_BACKEND = 'redis://localhost:6379' 
CELERY_ALWAYS_EAGER=True
CELERY_ACCEPT_CONTENT =["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER ="json"
CELERY_TIMEZONE = "UTC"
CELERY_STORE_ERRORS_EVEN_IF_IGNORED = True
CELERY_IGNORE_RESULT = False
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
CELERY_TASK_TIME_LIMIT= 30*60
CELERY_TASK_REJECT_ON_WORKER_LOST = True
CELERY_TASK_TRACK_STARTED = True
CELERY_ACKS_LATE = True
CELERY_WORKER_SEND_TASK_EVENTS = True
CELERY_TASK_SEND_SENT_EVENT = True
CELERY_TASK_TRACK_STARTED = True
