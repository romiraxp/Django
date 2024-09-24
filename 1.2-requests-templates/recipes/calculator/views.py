from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def recipes_view(request, dish):
    # по умолчанию serving = 1 и расчет будет произволдиться из расчета на 1 порцию
    serving = int(request.GET.get("serving", 1))
    template_name = 'calculator/index.html'
    try:
        recipe = {} # создадим подменный словарь для вывода рассчитаных значений
        # по выбранному блюду берем ингредиент и его кол-во
        for ingredient, amount in DATA[dish].items():
            # добавляем этот ингредиент и с перемноженным количеством
            recipe.setdefault(ingredient, amount * serving)
        context = {
            'recipe': recipe,
            'serving': serving
        }
    except KeyError:
        context = {
        }
    return render(request, template_name, context)
