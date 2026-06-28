from .env import DJANGO_ENV


if DJANGO_ENV == "production":
    from .production import LOGGING
elif DJANGO_ENV == "staging":
    from .staging import LOGGING
else:
    from .development import LOGGING


__all__ = ["LOGGING"]
