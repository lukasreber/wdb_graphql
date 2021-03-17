import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q

from .models import Ad, AdUser

class AdsType(DjangoObjectType):
    class Meta:
        model = Ad

class AdUsersType(DjangoObjectType):
    class Meta:
        model = AdUser

class Query(graphene.ObjectType):
    ads = graphene.List(
        AdsType, 
        search=graphene.String(),
        first=graphene.Int(),
        skip=graphene.Int(),
        )
    adusers = graphene.List(AdUsersType)

    def resolve_ads(self, into, search=None, first=None, skip=None, **kwargs):
        qs = Ad.objects.all()

        if search:
            filter = (
                Q(title__icontains=search) |
                Q(description__icontains=search)
            )
            return Ad.objects.filter(filter)

        if skip:
            qs = qs[skip:]

        if first:
            qs = qs[:first]

        return qs

    def resolve_adusers(self, into, **kwargs):
        return AdUser.objects.all()

class CreateAd(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    description = graphene.String()
    url = graphene.String()
    user = graphene.Field(AdUsersType)

    class Arguments:
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()
        user_name = graphene.String()

    def mutate(self, info, title, description, url, user_name):

        user = AdUser.objects.filter(name=user_name).first()
        if not user:
            raise Exception('Invalid User!')

        ad = Ad(title=title, description=description, url=url, user=user)
        ad.save()

        return CreateAd(
            id=ad.id,
            title=ad.title,
            description=ad.description,
            url=ad.url,
            user=ad.user
        )

class CreateAdUser(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()

    class Arguments:
        name = graphene.String()

    def mutate(self, info, name):
        aduser = AdUser(name=name)
        aduser.save()

        return CreateAdUser(
            id=aduser.id,
            name=aduser.name
        )

class DeleteAd(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        ad = Ad.objects.get(id=id)
        ad.delete()

        return DeleteAd(ok=True)

class DeleteAdUser(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        aduser = AdUser.objects.get(id=id)
        aduser.delete()

        return DeleteAdUser(ok=True)

class UpdateAd(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    description = graphene.String()
    url = graphene.String()
    #user = graphene.Field(AdUsersType)

    class Arguments:
        id = graphene.Int()
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()

    def mutate(self, info, id, title, description, url):
        ad = Ad.objects.get(id=id)
        ad.title = title
        ad.description = description
        ad.url = url
        ad.save()

        return UpdateAd(id=ad.id,
            title=ad.title,
            description=ad.description,
            url=ad.url)
            #user=ad.user)


class Mutation(graphene.ObjectType):
    create_ad = CreateAd.Field()
    create_aduser = CreateAdUser.Field()
    delete_ad = DeleteAd.Field()
    delete_aduser = DeleteAdUser.Field()
    update_ad = UpdateAd.Field()
        

# Update Ad + Tests
# Update Ad User + Tests
