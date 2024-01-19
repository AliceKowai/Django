from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('delete/<int:id>', views.delete_comida, name='delete'),
]
