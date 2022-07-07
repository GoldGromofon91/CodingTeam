import random

from django.core.management.base import BaseCommand
from food.models import Food, FoodCategory

CATEGORY_DATA = ['Напитки', 'Выпечка', 'Закуски']
FOOD_DATA = {
    'Напитки': ['Чай', 'Тархун', 'Байкал', 'Fanta'],
    'Выпечка': ['Хлеб'],
    'Закуски': ['Икра']
}


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Чистим предварительно БД
        try:
            Food.objects.all().delete()
            FoodCategory.objects.all().delete()
        except Exception as err:
            raise Exception(f'{err}\nОтчистите БД в ручную')

        category_data_for_bulk = []
        food_data_for_bulk = []

        for idx, el in enumerate(CATEGORY_DATA, 1):
            category_data_for_bulk.append(FoodCategory(name_ru=el, order_id=idx))

        FoodCategory.objects.bulk_create(category_data_for_bulk)

        qs = FoodCategory.objects.all()
        for elem in qs:
            if elem.name_ru in FOOD_DATA:
                for item in FOOD_DATA[elem.name_ru]:
                    food_data_for_bulk.append(
                        Food(name_ru=item,
                             is_vegan=random.choice([0, 1]),
                             is_special=random.choice([0, 1]),
                             code=random.choice([100, 110]),
                             cost=random.choice([100, 300]),
                             is_publish=random.choice([0, 1]),
                             category_id=elem.id
                             )
                    )

        Food.objects.bulk_create(food_data_for_bulk)
        print('БД заполнена тестовыми данными')
