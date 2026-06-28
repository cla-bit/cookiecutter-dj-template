from .base import *  # noqa: F403

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")  # noqa: F405

# SECURITY WARNING: don't run with debug turned on in production!.
DEBUG = False  # Set DEBUG to os.getenv("DEBUG")

# add this in the ALLOWED_HOSTS env variable for prod environment: avetiumbackupservice.avetiumconsult.com,161.35.165.249,backup-coral.vercel.app
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")  # noqa: F405

FRONTEND_BASE_URL = os.getenv("FRONTEND_BASE_URL")  # noqa: F405

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  # noqa: F405  # For production

# cors settings
CORS_ALLOWED_ORIGINS = []

# csrf settings
CSRF_TRUSTED_ORIGINS = []

CORS_ALLOW_CREDENTIALS = True  # only if using cookies from frontend
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SESSION_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = False  # must remain False for browsers to send it

# Clickjacking protection - Prevents UI redress, clickjacking attacks
X_FRAME_OPTIONS = "DENY"

# Referrer privacy - stops leaking sensitive urls
SECURE_REFERRER_POLICY = "strict-origin"

# Browser security headers - reduces MIME-sniffing attacks
SECURE_BROWSER_XSS_FILTER = True  # legacy browsers
SECURE_CONTENT_TYPE_NOSNIFF = True
