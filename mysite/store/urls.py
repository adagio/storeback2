#from django.urls import path, include
from django.conf.urls import url, include
from django.urls import re_path
from rest_framework.routers import DefaultRouter
from .store_api import BrandViewSet, ProductViewSet
from . import views
from .views import AireAcondicionadoListView

router = DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    re_path(r'^aire-acondicionado$', AireAcondicionadoListView.as_view(), name='aire_condicionado'),
    url(r'^api/', include(router.urls)),
]

