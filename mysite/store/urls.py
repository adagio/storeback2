#from django.urls import path, include
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .store_api import BrandViewSet, ProductViewSet
from . import views

router = DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/', include(router.urls)),
]

