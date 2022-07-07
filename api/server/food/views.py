from django.db.models import Prefetch
from rest_framework.viewsets import ModelViewSet
from .models import FoodCategory, Food
from .serializers import FoodListSerializer


class FoodCategoryView(ModelViewSet):
    """ Контроллер, отображения данных модели FoodCategory"""
    queryset = FoodCategory.objects.all()
    serializer_class = FoodListSerializer

    def get_queryset(self):
        # Переопределяем базовый метод получения queryset
        qs = FoodCategory.objects.filter(food__is_publish=True).prefetch_related(
                Prefetch("food", queryset=Food.objects.filter(is_publish=True))
            ).distinct()

        return qs
