from rest_framework import serializers
from basic.models.models import Topping, Pizza, Zakaz


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ('__all__')


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('__all__')


class ZakazSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zakaz
        fields = ('__all__')
