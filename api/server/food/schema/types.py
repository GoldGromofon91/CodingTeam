import graphene
from graphene_django import DjangoObjectType

from food.models import FoodCategory, Food


class FoodType(DjangoObjectType):
    """
    Класс описания модели blog.models.Food для graphene
    Meta:
        model = модель blog.models.Food
        fields = все поля модели blog.models.Food
    """

    class Meta:
        model = Food
        fields = "__all__"


class FoodCategoryType(DjangoObjectType):
    """
    Класс описания модели blog.models.FoodCategory для graphene
    Meta:
        model = модель blog.models.FoodCategory
        fields = все поля модели blog.models.FoodCategory
    """

    class Meta:
        model = FoodCategory
        fields = "__all__"

    foods = graphene.List(FoodType)

    def resolve_foods(root, info):
        qs = Food.objects.filter(category=root, is_publish=True)
        return qs