from django.urls import path,include
from realative_url_app import views

urlpatterns = [
    path('second/', views.second, name='second'),
    path('third/', views.third, name='third'),
    path('index/', views.index, name='index'),

    ]
