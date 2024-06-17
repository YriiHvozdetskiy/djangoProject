from django.shortcuts import render


def index(request):
    # context - зараз як база даних
    context = {
        'title': 'goods',
        'content': "goods page",
    }

    return render(request, 'goods/index.html', context)
