from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EmployeeView, ProductView, OrderView


router = DefaultRouter()


router.register('employes', EmployeeView)
router.register('products', ProductView)
router.register('orders', OrderView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
