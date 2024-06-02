from django.http import HttpResponse
from django.shortcuts import render

"""
views - це контролер/представленя/інтерфейс в патерні MVC
звязує частину яку ми бачимо з models
- виконують прийом запитів від користувача і передачу відповіді користувачу
"""


def index(request):
    # контекст потрапляє в templates
    context = {
        'title': 'Home - Главная',
        'content': "Магазин мебели HOME",
    }
    return render(request, 'core/index.html', context)


def about(request):
    return HttpResponse('About page')
