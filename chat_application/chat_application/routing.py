from django.urls import path, include, re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    # path("/ws/<room_slug>", ChatConsumer.as_asgi()),
    re_path(r'^ws/(?P<room_slug>[^/]+)/$', ChatConsumer.as_asgi()),
]