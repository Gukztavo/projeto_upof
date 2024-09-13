
from django.contrib import admin
from django.urls import path
from app_upof import views

urlpatterns = [

    #rota, view resposanvel, nome de referencia
    path('',views.home,name='home'),
]
