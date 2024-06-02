from django.http import HttpResponse
from django.shortcuts import render

"""
views - це контролер/представленя/інтерфейс в патерні MVC
звязує частину яку ми бачимо з models
- виконують прийом запитів від користувача і передачу відповіді користувачу
"""


def index(request):
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('About page')
