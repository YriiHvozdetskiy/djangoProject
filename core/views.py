from django.http import HttpResponse
from django.shortcuts import render

"""
views - це контролер/представленя/інтерфейс в патерні MVC
звязує частину яку ми бачимо з models(база даних)
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
    # пишем саме так: text_on_page
    context = {
        'title': 'Home - О нас',
        'content': "О нас",
        'text_on_page': "Текст о том почему этот магазин такой классный, и какой хороший товар."
    }

    return render(request, 'core/about.html', context)
