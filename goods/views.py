from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet


def index(request):
    # context - зараз як база даних
    context = {
        'title': 'goods',
        'content': "goods page",
    }

    return render(request, 'goods/index.html', context)
