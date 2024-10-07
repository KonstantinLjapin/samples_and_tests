[
    {
        "id": 1,
        "name_ru": "Напитки",
        "name_en": null,
        "name_ch": null,
        "order_id": 10,
        "foods": [
            {
                "internal_code": 100,
                "code": 1,
                "name_ru": "Чай",
                "description_ru": "Чай 100 гр",
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": false,
                "cost": "123.00",
                "additional": [
                    200
                ]
            },
            {
                "internal_code": 200,
                "code": 2,
                "name_ru": "Кола",
                "description_ru": "Кола",
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": false,
                "cost": "123.00",
                "additional": [

                ]
            },
            {
                "internal_code": 300,
                "code": 3,
                "name_ru": "Спрайт",
                "description_ru": "Спрайт",
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": false,
                "cost": "123.00",
                "additional": [

                ]
            },
            {
                "internal_code": 400,
                "code": 4,
                "name_ru": "Байкал",
                "description_ru": "Байкал",
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": false,
                "cost": "123.00",
                "additional": [

                ]
            }
        ]
    },
    {
        "id": 2,
        "name_ru": "Выпечка",
        "name_en": null,
        "name_ch": null,
        "order_id": 20,
        "foods": [...]
    },
    {...},
    {...}
]

# models.py

from django.db import models
from model_utils.models import TimeStampedModel
from rest_framework import serializers


class FoodCategory(TimeStampedModel):
    name_ru = models.CharField(verbose_name='Название на русском', max_length=255, unique=True)
    name_en = models.CharField(verbose_name='Название на английском', max_length=255,
                               unique=True, blank=True, null=True)
    name_ch = models.CharField(verbose_name='Название на китайском', max_length=255,
                               unique=True, blank=True, null=True)
    order_id = models.SmallIntegerField(default=10, blank=True, null=True)

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Раздел меню'
        verbose_name_plural = 'Разделы меню'
        ordering = ('name_ru', 'order_id')


class Food(TimeStampedModel):
    category = models.ForeignKey(FoodCategory, verbose_name='Раздел меню',
                                 related_name='food', on_delete=models.CASCADE)

    is_vegan = models.BooleanField(verbose_name='Вегетарианское меню', default=False)
    is_special = models.BooleanField(verbose_name='Специальное предложение', default=False)

    code = models.IntegerField(verbose_name='Код поставщика')
    internal_code = models.IntegerField(verbose_name='Код в приложении', unique=True, null=True, blank=True)

    name_ru = models.CharField(verbose_name='Название на русском', max_length=255)
    description_ru = models.CharField(verbose_name='Описание на русском', max_length=255, blank=True, null=True)
    description_en = models.CharField(verbose_name='Описание на английском', max_length=255, blank=True, null=True)
    description_ch = models.CharField(verbose_name='Описание на китайском', max_length=255, blank=True, null=True)

    cost = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)

    is_publish = models.BooleanField(verbose_name='Опубликовано', default=True)

    additional = models.ManyToManyField('self', verbose_name='Дополнительные товары', symmetrical=False,
                                        related_name='additional_from', blank=True)

    def __str__(self):
        return self.name_ru


class FoodSerializer(serializers.ModelSerializer):
    additional = serializers.SlugRelatedField(many=True, read_only=True, slug_field='internal_code')

    class Meta:
        model = Food
        fields = ('internal_code', 'code', 'name_ru', 'description_ru', 'description_en',
                  'description_ch', 'is_vegan', 'is_special', 'cost', 'additional')


class FoodListSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(source='food', many=True, read_only=True)

    class Meta:
        model = FoodCategory
        fields = ('id', 'name_ru', 'name_en', 'name_ch', 'order_id', 'foods')

# Предлагаю решение тестового задания, первый раз сталкиваюсь с неполной реализацией
# TimeStampedModel вижу в первый раз )) создавая реализацию для вью я бы написал сериализаторы возможно нужно применить
# пагинацию при большом количестве элементов
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FoodCategory, Food
from .serializers import CategorySerializer, FoodSerializer

from rest_framework import serializers


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['internal_code', 'code', 'name_ru', 'description_ru', 'description_en', 'description_ch',
                  'is_vegan', 'is_special', 'cost', 'additional']

class CategorySerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True, read_only=True)

    class Meta:
        model = FoodCategory
        fields = ['id', 'name_ru', 'name_en', 'name_ch', 'order_id', 'foods']


class FoodListView(APIView):
    def get(self, request):
        categories = FoodCategory.objects.filter(foods__is_publish=True).prefetch_related('foods')

        result = []
        for category in categories:
            foods = category.foods.filter(is_publish=True)  # Фильтруем блюда по is_publish
            food_data = FoodSerializer(foods, many=True).data  # Сериализуем блюда

            result.append({
                "id": category.id,
                "name_ru": category.name_ru,
                "name_en": category.name_en,
                "name_ch": category.name_ch,
                "order_id": category.order_id,
                "foods": food_data
            })

        return Response(result)
