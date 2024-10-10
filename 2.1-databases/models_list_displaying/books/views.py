from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from books.models import Book
from datetime import datetime


def books_view(request):
    template = 'books/books_list.html'
    all_books = Book.objects.all()
    context = {'books': all_books}
#    print(context)
    return render(request, template, context)

def a_book_view(request, dt: datetime):
    # будем использовать новый шаблон, на странице которого будет отображаться информация по книгам на выбранную дату
    template = 'books/a_book.html'
    # в переменную 'selected_date' будем помещать результат выборки
    selected_date = Book.objects.filter(pub_date = dt)
    # для пагинации запросим весь список объектов
    all_books = Book.objects.all()

    page_number = request.GET.get(dt)
    paginator = Paginator(all_books,1)
    page = paginator.get_page(page_number)

    # в переменные 'date_before' и 'date_after' будем помещать дату ДО и ПОСЛЕ указанной даты.
    # Для этого отсортируем их и возьмем рядом стоящие даты от указанной
    date_before = Book.objects.filter(pub_date__lt=dt).values('pub_date').order_by('pub_date').last()
    date_after = Book.objects.filter(pub_date__gt=dt).values('pub_date').order_by('pub_date').first()

    # чтобы избежать ошибок добавляем проверку на случаи, когда дата ДО и ПОСЛЕ могут быть пустыми,
    # а также передаем их в контексте
    if date_before and date_after:
        context = {'a_book': selected_date,
                   'page': page,
                   'page_next': date_after['pub_date'],
                   'page_prev': date_before['pub_date'],
                   }
    elif date_before is None:
        context = {'a_book': selected_date,
                   'page': page,
                   'page_next': date_after['pub_date'],
                   }
    elif date_after is None:
        context = {'a_book': selected_date,
                   'page': page,
                   'page_prev': date_before['pub_date'],
                   }
    return render(request, template, context)
