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
    # attributes which are returned
    id = graphene.Int()
    nr = graphene.Int()
    title = graphene.String()
    price = graphene.Int()
    zipcode = graphene.Int()
    description = graphene.String()
    category = graphene.String()
    url = graphene.String()
    dateadded = graphene.String()
    views = graphene.Int()
    user = graphene.Field(AdUsersType)

    # attributes to be used in the mutation
    class Arguments:
        nr = graphene.Int()
        title = graphene.String()
        price = graphene.Int()
        zipcode = graphene.Int()
        description = graphene.String()
        category = graphene.String()
        url = graphene.String()
        dateadded = graphene.String()
        views = graphene.Int()
        user_name = graphene.String()

    def mutate(self, info, nr, title, price, zipcode, description, category, url, dateadded, views, user_name):

        # check if the submited user exists, if not raise an error
        user = AdUser.objects.filter(name=user_name).first()
        if not user:
            raise Exception('Invalid User!')
        
        # add the new entry to the database
        ad = Ad(nr=nr, title=title, price=price, zipcode=zipcode, description=description, category=category, url=url, dateadded=dateadded, views=views, user=user)
        ad.save()

        # return all the attributes
        return CreateAd(
            id=ad.id,
            nr=ad.nr,
            title=ad.title,
            price=ad.price,
            description=ad.description,
            category=ad.category,
            url=ad.url,
            user=ad.user
        )

class CreateAdUser(graphene.Mutation):
    # attributes which are returned
    id = graphene.Int()
    name = graphene.String()

    # attributes to be used in the mutation
    class Arguments:
        name = graphene.String()

    def mutate(self, info, name):
        # add new user to the database
        aduser = AdUser(name=name)
        aduser.save()

        return CreateAdUser(
            id=aduser.id,
            name=aduser.name
        )

class DeleteAd(graphene.Mutation):
    # attributes which are returned
    ok = graphene.Boolean()

    # attributes to be used in the mutation
    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        # delete ad with id provided
        ad = Ad.objects.get(id=id)
        ad.delete()

        return DeleteAd(ok=True)

class DeleteAdUser(graphene.Mutation):
    # attributes which are returned
    ok = graphene.Boolean()

    # attributes to be used in the mutation
    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        # delete user with id provided
        aduser = AdUser.objects.get(id=id)
        aduser.delete()

        return DeleteAdUser(ok=True)

class UpdateAd(graphene.Mutation):
    # attributes which are returned
    id = graphene.Int()
    title = graphene.String()
    description = graphene.String()
    url = graphene.String()

    # attributes to be used in the mutation
    class Arguments:
        id = graphene.Int()
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()

    def mutate(self, info, id, **kwargs):
        # get ad with id from database
        ad = Ad.objects.get(id=id)

        # for each other attribte, if not empty, update the value, otherwise do nothing
        if kwargs.get('title'):
            ad.title = kwargs.get('title', None)
        if kwargs.get('description'):
            ad.description = kwargs.get('description', None)
        if kwargs.get('url'):
            ad.url = kwargs.get('url', None)
        ad.save()

        return UpdateAd(
            id=ad.id,
            title=ad.title,
            description=ad.description,
            url=ad.url
        )

class UpdateAdUser(graphene.Mutation):
    # attributes which are returned
    id = graphene.Int()
    name = graphene.String()

    # attributes to be used in the mutation
    class Arguments:
        id = graphene.Int()
        name = graphene.String()

    def mutate(self, info, id, name):
        # get user with id provided
        aduser = AdUser.objects.get(id=id)
        # update name with new value
        aduser.name = name
        aduser.save()

        return UpdateAdUser(
            id=aduser.id,
            name=aduser.name,
        )

class Mutation(graphene.ObjectType):
    create_ad = CreateAd.Field()
    create_aduser = CreateAdUser.Field()
    delete_ad = DeleteAd.Field()
    delete_aduser = DeleteAdUser.Field()
    update_ad = UpdateAd.Field()
    update_aduser = UpdateAdUser.Field()

