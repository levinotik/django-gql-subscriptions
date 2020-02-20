import graphene

from subscriptions.graphql import HelloSubscription


class Query(graphene.ObjectType):
    base = graphene.String()


class Subscription(HelloSubscription):
    pass


schema = graphene.Schema(
    query=Query,
    subscription=Subscription
)
