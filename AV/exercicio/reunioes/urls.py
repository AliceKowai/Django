from django.urls import path, include
from .views import index, register, delete_reuniao

from rest_framework import routers
from .api.viewsets import ReunioesViewSet
router = routers.DefaultRouter()
router.register(r'reunioes', ReunioesViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('delete/<int:id>', delete_reuniao, name='delete'),
    path('api_reunioes', include(router.urls))

]
