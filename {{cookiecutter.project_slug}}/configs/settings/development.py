from .base import *  # noqa: F403


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")  # noqa: F405

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

{% if cookiecutter.use_postgresql == "yes" %}
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),  # noqa: F405
        "USER": os.getenv("POSTGRES_USER"),  # noqa: F405
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),  # noqa: F405
        "HOST": os.getenv("POSTGRES_HOST", "localhost"),  # noqa: F405
        "PORT": os.getenv("POSTGRES_PORT", "5432"),  # noqa: F405
        "OPTIONS": {
            "sslmode": os.getenv("POSTGRES_SSLMODE", "require"),  # noqa: F405
        },
    }
}
{% else %}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # noqa: F405
    }
}
{% endif %}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]  # noqa: F405  # For development
