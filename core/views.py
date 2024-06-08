from django.http import HttpResponse
from django.shortcuts import render

"""
views - це контролер/представленя/інтерфейс в патерні MVC
звязує частину яку ми бачимо з models
- виконують прийом запитів від користувача і передачу відповіді користувачу
"""


def index(request):
    # контекст потрапляє в templates
    # context - зараз як база даних
    context = {
        'title': 'Home - Главная',
        'content': "Магазин мебели HOME",
        'list': ['list'],
        'dict': {'first': 1},
        'is_auth': True,
        'user_name': 'Kote'
    }
    return render(request, 'core/index.html', context)


def about(request):
    return HttpResponse('About page')
