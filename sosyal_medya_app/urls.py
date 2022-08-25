from django.urls import path
from . import views

urlpatterns = [

    path('', views.anasayfa, name = 'anasayfa'),
    path('anasayfa', views.anasayfa, name = 'anasayfa'),
    path('kayit', views.kayit, name = 'kayit'),
    path('paylas', views.paylas, name = 'paylas'),
]