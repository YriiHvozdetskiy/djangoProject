"""
корневий urls

підключаєм urls з інших файлів конфігурації: core...

"""

from django.contrib import admin
from django.urls import path, include

"""
include - ф-ція підключає на загальний(config) url маршрут інші приложенія

namespace - записуєм до якого приложенія відносяться urls адреса коли ми звертаємось до них в шаблонах:
<a href="{% url "core:index" %}">Home</a> - це в base.html

"""
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('core.urls', namespace='core'))
]
