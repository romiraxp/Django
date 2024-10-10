from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_phones = request.GET.get('sort')
    all_phones = Phone.objects.all()

    if sort_phones == 'name':
        sorted_phones_by_name = all_phones.order_by('name')
        context = {'phones': sorted_phones_by_name,
                   }
        return render(request, template, context)
    elif sort_phones == 'min_price':
        sorted_phones_by_price = all_phones.order_by('price')
        context = {'phones': sorted_phones_by_price
                   }
        return render(request, template, context)
    elif sort_phones == 'max_price':
        sorted_phones_by_price = all_phones.order_by('-price')
        context = {'phones': sorted_phones_by_price
                   }
        return render(request, template, context)

    context = {'phones': all_phones,
               }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    requested_model = Phone.objects.get(slug = slug)
    context = {'phone': requested_model,
               }
    return render(request, template, context)
