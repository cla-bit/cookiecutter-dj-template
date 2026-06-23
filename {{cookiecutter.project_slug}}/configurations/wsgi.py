"""
WSGI config for template project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application

from configurations.env import load_environment


load_environment()

application = get_wsgi_application()
