import json
from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):
    help = 'Заполнение БД данными из Json файла'
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('fixtures/books.json', 'r', encoding='UTF-8') as json_file:
            books = json.load(json_file)
            # print(books)
            #list(csv.DictReader(file, delimiter=';'))
        for book in books:
            # print(book)
            # TODO: Добавьте сохранение модели
            book_name = Book.objects.create(
                id = book['pk'],
                name = book['fields']['name'],
                author = book['fields']['author'],
                pub_date = book['fields']['pub_date'],
                #slug = slugify(book['fields']['name']),
            )
            book_name.save
