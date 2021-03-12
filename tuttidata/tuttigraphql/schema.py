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

class CreateAd(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    description = graphene.String()
    url = graphene.String()

    class Arguments:
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()

    def mutate(self, info, title, description, url):
        ads = Ads(title=title, description=description, url=url)
        ads.save()

        return CreateAd(
            id=ads.id,
            title=ads.title,
            description=ads.description,
            url=ads.url,
        )
class Mutation(graphene.ObjectType):
    create_ad = CreateAd.Field()
        