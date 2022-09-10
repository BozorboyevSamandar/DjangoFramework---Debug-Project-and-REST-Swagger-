from django.urls import path, include
from .views import ZakazViewSet, PizzaViewSet, ToppingViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('zakaz', ZakazViewSet)
router.register('pizza', PizzaViewSet)
router.register('topping', ToppingViewSet)

urlpatterns = [
    path('', include(router.urls))
]
