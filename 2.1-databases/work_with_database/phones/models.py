from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.AutoField(verbose_name='ID', primary_key=True)
    name = models.CharField(verbose_name='Model', max_length=64)
    price = models.CharField(verbose_name='Price', max_length=6)
    image = models.URLField(verbose_name='Photo', max_length=250)
    release_date = models.DateField(verbose_name='Дата релиза')
    lte_exists = models.BooleanField(verbose_name='Наличие LTE')
    slug = models.SlugField(max_length=255, unique=True)
