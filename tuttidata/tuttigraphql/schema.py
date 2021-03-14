import graphene
from graphene_django import DjangoObjectType

from .models import Ad, AdUser

class AdsType(DjangoObjectType):
    class Meta:
        model = Ad

class AdUsersType(DjangoObjectType):
    class Meta:
        model = AdUser

class Query(graphene.ObjectType):
    ads = graphene.List(AdsType)
    adusers = graphene.List(AdUsersType)

    def resolve_ads(self, into, **kwargs):
        return Ad.objects.all()

    def resolve_adusers(self, into, **kwargs):
        return AdUser.objects.all()

class CreateAd(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    description = graphene.String()
    url = graphene.String()
    #user = graphene.String()

    class Arguments:
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()

    def mutate(self, info, title, description, url):
        ad = Ad(title=title, description=description, url=url)
        ad.save()

        return CreateAd(
            id=ad.id,
            title=ad.title,
            description=ad.description,
            url=ad.url,
        )




class Mutation(graphene.ObjectType):
    create_ad = CreateAd.Field()
        