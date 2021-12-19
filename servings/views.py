from django.shortcuts import render

# Create your views here.
def omlet(request):
    n = int(request.GET.get('servings', 1))
    context = {
        'omlet': {
            'яйца, шт': 2 * n,
            'молоко, л': round((0.1 * n),3),
            'соль, ч.л.': 0.5 * n,
        },
        'pasta': {
            'макароны, г': 0.3 * n,
            'сыр, г': 0.05 * n,
        },
        'buter': {
            'хлеб, ломтик': 1 * n,
            'колбаса, ломтик': 1 * n,
            'сыр, ломтик': 1 * n,
            'помидор, ломтик': 1 * n,
        },

    }
    return render(request,'omlet.html' , context)

def pasta(request):
    n = int(request.GET.get('servings', 1))
    context = {
        'omlet': {
            'яйца, шт': 2 * n,
            'молоко, л': round((0.1 * n), 3),
            'соль, ч.л.': 0.5 * n,
        },
        'pasta': {
            'макароны, г': 0.3 * n,
            'сыр, г': 0.05 * n,
        },
        'buter': {
            'хлеб, ломтик': 1 * n,
            'колбаса, ломтик': 1 * n,
            'сыр, ломтик': 1 * n,
            'помидор, ломтик': 1 * n,
        },

    }
    return render(request,'pasta.html' , context)

def buter(request):
    n = int(request.GET.get('servings', 1))
    context = {
        'omlet': {
            'яйца, шт': 2 * n,
            'молоко, л': round((0.1 * n), 3),
            'соль, ч.л.': 0.5 * n,
        },
        'pasta': {
            'макароны, г': 0.3 * n,
            'сыр, г': 0.05 * n,
        },
        'buter': {
            'хлеб, ломтик': 1 * n,
            'колбаса, ломтик': 1 * n,
            'сыр, ломтик': 1 * n,
            'помидор, ломтик': 1 * n,
        },

    }
    return render(request,'buter .html' , context)