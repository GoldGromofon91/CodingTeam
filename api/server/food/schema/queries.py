import graphene
from django.db.models import Q
from graphene_django.filter import DjangoFilterConnectionField

from food.models import FoodCategory
from food.schema.types import FoodCategoryType
from server.logger import LoggerDec


class FoodQuery(graphene.ObjectType):
    """
    Класс подключения запросов приложения `food`
    """

    # Все категории продуктов
    food_categories = graphene.List(FoodCategoryType)

    @LoggerDec()
    def resolve_food_categories(root, info):
        qs = FoodCategory.objects.all()
        return qs

