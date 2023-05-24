from django.shortcuts import render
import copy 

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

DATA_calc = copy.deepcopy(DATA)


def index(request, recipe):
    context = {} 
    servings = int(request.GET.get('servings', 1))
    if recipe in DATA:
        context = {'recipe': DATA[recipe]
                   }
        if servings > 1:
            for key, value in DATA[recipe].items():
                DATA_calc[recipe][key] = DATA[recipe][key]
                DATA_calc[recipe][key] = round(value * servings, 2)
                context = {'recipe': DATA_calc[recipe]}
    return render(request, 'calculator/index.html', context)

