import graphene
from graphene_django import DjangoObjectType

from .models import Ads

class AdsType(DjangoObjectType):
    class Meta:
        model = Ads


class Query(graphene.ObjectType):
    ads = graphene.List(AdsType)

    def resolve_ads(self, into, **kwargs):
        return Ads.objects.all()