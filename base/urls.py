from django.urls import path
from base import views

urlpatterns = [
    path('home', views.index, name='home_page')
]