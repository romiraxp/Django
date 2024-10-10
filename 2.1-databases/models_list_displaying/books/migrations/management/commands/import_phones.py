import csv
from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = 'Заполнение БД данными из CSV файла'
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            phone_model = Phone.objects.create(
                id = phone['id'],
                name = phone['name'],
                image = phone['image'],
                price = phone['price'],
                release_date = phone['release_date'],
                lte_exists = phone['lte_exists'],
                slug = slugify(phone['name']),
            )
            phone_model.save
            #print(phone_model.name, phone_model.slug)



