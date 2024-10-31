from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

# модель датчика Sensor
class Sensor(models.Model):
    name = models.CharField(verbose_name='Датчик') # название датчика
    description = models.TextField(null=True, blank=True, verbose_name='Описание') # краткое описание, в нашем случае местоположение датчика

    def __str__(self):
        return self.name
class Measurement(models.Model):
    temperature = models.FloatField(verbose_name='Температура')
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE,related_name='sensor',verbose_name='Датчик ID')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время измерения')
    image = models.ImageField(upload_to='upload/', null=True, blank=True, verbose_name='Изображение')
    def __str__(self):
        #return f"{self.temperature} {self.created_at}"
        return self.temperature

