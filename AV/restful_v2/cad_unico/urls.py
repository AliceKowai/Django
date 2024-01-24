from django.urls import include,path
from rest_framework import routers
from .api.viewsets import BeneficiariosViewSet

router = routers.DefaultRouter()
router.register(r'beneficiarios', BeneficiariosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
