"""
ASGI config for chatApp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from requests import URLRequired 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatApp.settings')
from App import routing  
# application = get_asgi_application()

application=ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter(
           routing.websocket_urlpatterns
        )
    )
})
