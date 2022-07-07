from django.db import models


class FoodCategory(models.Model):
    name_ru = models.CharField('Название на русском', max_length=255, unique=True)
    name_en = models.CharField('Название на английском', max_length=255, unique=True, blank=True, null=True)
    name_ch = models.CharField('Название на китайском', max_length=255, unique=True, blank=True, null=True)
    order_id = models.SmallIntegerField(default=10, blank=True, null=True)

    def __str__(self):
        return self.name_ru

    class Meta:
        db_table = 'food_category'
        verbose_name = 'Раздел меню'
        verbose_name_plural = 'Разделы меню'
        ordering = ('name_ru', 'order_id')


class Food(models.Model):
    is_vegan = models.BooleanField('Вегетарианское меню', default=False)
    is_special = models.BooleanField('Специальное предложение', default=False)
    code = models.IntegerField('Код поставщика')
    internal_code = models.IntegerField('Код в приложении', unique=True, null=True, blank=True)
    name_ru = models.CharField('Название на русском', max_length=255)
    description_ru = models.CharField('Описание на русском', max_length=255, blank=True, null=True)
    description_en = models.CharField('Описание на английском', max_length=255, blank=True, null=True)
    description_ch = models.CharField('Описание на китайском', max_length=255, blank=True, null=True)
    cost = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    is_publish = models.BooleanField('Опубликовано', default=True)

    category = models.ForeignKey(FoodCategory, verbose_name='Раздел меню', related_name='food', on_delete=models.CASCADE)
    additional = models.ManyToManyField('self', verbose_name='Дополнительные товары', symmetrical=False, related_name='additional_from', blank=True)

    class Meta:
        db_table = 'food'
        verbose_name = 'Блюда'
        verbose_name_plural = 'Разделы меню'
        ordering = ('name_ru', 'cost')

    def __str__(self):
        return self.name_ru
