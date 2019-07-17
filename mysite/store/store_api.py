from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import Brand, Product
from .serializers import BrandSerializer, ProductSerializer


class BaseViewSet (viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = self.queryset.filter()
        return qs

    def perform_create(self, serializer):
        serializer.save()

class BrandViewSet(BaseViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

class ProductViewSet(BaseViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

