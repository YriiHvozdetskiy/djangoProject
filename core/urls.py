from django.urls import path
from core import views

app_name = 'main'  # назва приложенія(використовується в навігації в templates)

urlpatterns = [
    path('', views.index, name='index'),  # '' === mysite.com
    path('about/', views.about, name='about'),  # about/ - адреса сторінки
]
