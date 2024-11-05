from django.db import transaction
from rest_framework import serializers
from .models import Product, Stock, StockProduct

class ProductSerializer(serializers.ModelSerializer):
#    positions = ProductPositionSerializer(many=True)
    # настройте сериализатор для продукта
    class Meta:
        model = Product
        fields = ['title', 'description']

class ProductPositionSerializer(serializers.ModelSerializer):
    #positions = ProductSerializer()
    # настройте сериализатор для позиции продукта на складе
    class Meta:
        model = StockProduct
#        fields = ['product', 'quantity', 'price', 'positions']
        fields = ['product', 'quantity', 'price']

class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    # настройте сериализатор для склада
    class Meta:
        model = Stock
        fields = ['address', 'positions']

    @transaction.atomic
    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions', [])

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        StockProduct.objects.bulk_create([StockProduct(stock=stock, **position) for position in positions])
        # for position in positions:
        #     StockProduct.objects.create(stock=stock, **position)

        return stock

    @transaction.atomic
    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        # способ Александра это удалить и заново создать с 0
        positions = validated_data.pop('positions', [])
        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)
        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        instance.positions.all().delete()
        StockProduct.objects.bulk_create([StockProduct(stock=stock, **position) for position in positions])
        return stock

        # positions_data = validated_data.pop('positions', [])
        # positions = (instance.positions).all()
        # positions = list(positions)
        # print(list(positions_data))
        # print(positions)
        # instance.address = validated_data.get('address', instance.address)
        # print(instance.address)
        # instance.quantity = validated_data.get('quantity', instance.quantity)
        # instance.price = validated_data.get('price', instance.price)
        # instance.save()

        # for position_data in positions_data:
        #     position = positions.pop(0)
        #     position.product = position_data.get('product', position.product)
        #     position.quantity = position_data.get('quantity', position.quantity)
        #     position.price = position_data.get('price', position.price)
        #     position.save()
            # StockProduct.objects.update(stock=stock, **position)
        # return instance
