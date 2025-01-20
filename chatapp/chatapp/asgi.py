"""
ASGI config for chatapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

# chatapp/asgi.py

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
# from chat.routing import websocket_urlpatterns  # import WebSocket URLs
from chat.consumers import ChatConsumer  # Import the consumer class
from django.urls import re_path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapp.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),  # Use the WebSocket URL routing
        )
    ),
})
