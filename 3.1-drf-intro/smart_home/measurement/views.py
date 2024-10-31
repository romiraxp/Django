# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView# RetrieveAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementsSerializer, SensorDetailSerializer

# с использованием ListAPIView
# для получения информации о всех датчиках
class SensorsView(ListAPIView):
    queryset = Sensor.objects.all() # нужно указать откуда взять данные и для этого используется queryset
    serializer_class = SensorSerializer  # и второе с помощью чего нужно набор этих объектов превратить в JSON, т.е. указать сериализатор
    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# для отображения датчика и соответствующих ему изменрений
# для получения информации по одному какому- то элементу используетс RetrieveAPIView
class SensorRetrView(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()     # здесь также укажем queryset - откуда взять данные
    serializer_class = SensorDetailSerializer     # и сериализатор для конвертации в JSON
    # после чего нужно зарегистрировать данный view- класс и прописать его в urls.py

    def patch(self,request, pk):
        sensor_id = Sensor.objects.get(id= pk)  # получаем объект по полю ID
        serializer = SensorDetailSerializer(sensor_id, data=request.data, partial=True) # сериализируем его
        if serializer.is_valid(): # если такой существует и валидный, то производим замену
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_304_NOT_MODIFIED)

# для получения информации об измерениях из таблицы измерений Measurement
class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all() # нужно указать откуда взять данные и для этого используется queryset
    serializer_class = MeasurementsSerializer # и второе с помощью чего нужно набор этих объектов превратить в JSON, т.е. указать сериализатор
# аналогичное добавление
    def post(self, request):
        serializer = MeasurementsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
