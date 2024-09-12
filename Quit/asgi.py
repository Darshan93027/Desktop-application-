"""
ASGI config for Quit project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Quit.settings')

# Django application setup
application = get_asgi_application()

# WebSocket routing pattern
ws_patterns = [
    # Add your WebSocket URL routes here
    # path('ws/some_path/', SomeConsumer.as_asgi()),
]

# ASGI application setup
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(ws_patterns),
})
