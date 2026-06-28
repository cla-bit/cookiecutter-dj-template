"""
ASGI config for template project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

from django.core.asgi import get_asgi_application

from configs.env import load_environment


load_environment()

application = get_asgi_application()
