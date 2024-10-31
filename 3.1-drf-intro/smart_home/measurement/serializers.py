from rest_framework import serializers
from .models import Sensor, Measurement
# TODO: опишите необходимые сериализаторы
# class SensorSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     description = serializers.CharField()

# класс ModelSerializer используется, если сериалайзер является чуть ли копией модели
class SensorSerializer(serializers.ModelSerializer):
    # для того чтобы указать на основе какой модели строить сериалазер нужно испоьзовать внутренний класс Meta
    class Meta:
        model = Sensor # указываем модель и ее нужно импортировать
        fields = '__all__'
#class MeasurementsSerializer(serializers.Serializer):
# изменил здесь на ModelSerializer, т.к. просто с Serializer не работало, выводило пустые значения измерений


class MeasurementsSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Measurement
        #fields = ['temperature', 'created_at','sensor']
        fields = ['temperature', 'created_at','image','sensor']

class SensorDetailSerializer(serializers.ModelSerializer):
    #measurements = MeasurementSerializer(read_only=True, many=True)
    sensor = MeasurementsSerializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        #fields = ['id', 'name', 'description', 'sensor']
        fields = ['id', 'name', 'description', 'sensor']