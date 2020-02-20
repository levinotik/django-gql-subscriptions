from .wsgi import *  # add this line to top of your code
from .asgi import *
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from graphene_subscriptions.consumers import GraphqlSubscriptionConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path('graphql/', GraphqlSubscriptionConsumer)
    ]),
})