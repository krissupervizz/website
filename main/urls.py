from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "reg"),
    path('vh', views.vh, name = "vh"),
    path('landing', views.landing, name = 'landing'),
    path('lk', views.lk, name = 'lk'),
]