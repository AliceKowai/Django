from django.urls import path, include
from .views import index
from .views import register

urlpatterns = [
    path('', index, name='index'),
    path('register_atracoes_turisticas', register, name='register_atracoes_turisticas'),

]
