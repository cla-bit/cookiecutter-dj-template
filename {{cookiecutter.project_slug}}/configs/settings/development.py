from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ cookiecutter.django_secret_key }}'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

{% if cookiecutter.use_postgresql == "yes" %}
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST", "localhost"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
        "OPTIONS": {
            "sslmode": os.getenv("POSTGRES_SSLMODE", "require"),
        },
    }
}
{% else %}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
{% endif %}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]  # For development
