from django.urls import path
from . import views


urlpatterns = [
    path('', views.main , name = 'main'),
    path('login/', views.login , name = 'login'),
    path('prices/', views.prices, name = 'prices'),
    path('insert', views.insert, name='insert'),
    path('products/', views.products, name = 'products'),
    path('send/' , views.send_message, name = 'send'),

    ]
