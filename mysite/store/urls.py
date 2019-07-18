#from django.urls import path, include
from django.conf.urls import url, include
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from .store_api import BrandViewSet, ProductViewSet
from . import views
from .views import ProductListView
from .views import ProductDetailView
from .views import CategoryListView
from .views import CategoryDetailView
from .views import ProductListByCategoryView

router = DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    re_path(r'^products$', ProductListView.as_view(), name='product-list'),
    url(r'^api/', include(router.urls)),
    path('p/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('categories', CategoryListView.as_view(), name='category-list'),
    path('c/<int:pk>', CategoryDetailView.as_view(), name='category-detail'),
    path('cp/<int:category_id>', ProductListByCategoryView.as_view(),
    name='products-by-category')
]

