import graphene

import topdiez.schema


class Query(topdiez.schema.Query, graphene.ObjectType):
    pass

class Mutation(topdiez.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query,mutation=Mutation)
