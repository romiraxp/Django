# coding=utf-8

from django.db import models


class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(u'Название', max_length=64)
    author = models.CharField(u'Автор', max_length=64)
    pub_date = models.DateTimeField(u'Дата публикации')
    #slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name + " " + self.author