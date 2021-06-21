from django.urls import path
from narguile import views

urlpatterns = [
    path('', views.list_all, name='list_all'),
    path('create', views.create, name='create_narguile'),
    path('update/<int:id>', views.update, name='update_narguile'),
    path('delete/<int:id>', views.delete, name='delete_narguile'),
]