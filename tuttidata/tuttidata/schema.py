import graphene

import tuttigraphql.schema

class Query(tuttigraphql.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)