from django.urls import path
from narguile import views

urlpatterns = [
    path('', views.list_all, name='list_all')
]