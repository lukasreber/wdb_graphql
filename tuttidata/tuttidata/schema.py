import graphene

import tuttigraphql.schema

class Query(Ads.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)