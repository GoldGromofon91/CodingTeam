import graphene

from food.schema.queries import FoodQuery


class Query(FoodQuery, graphene.ObjectType):
    """
    Класс подключения к корневой схеме GraphQL, описанных запросов для каждого приложения
    """
    pass


schema = graphene.Schema(query=Query)
