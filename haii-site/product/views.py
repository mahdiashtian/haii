from unittest import result
from rest_framework import viewsets
from .models import Product
from .serializers_ import ProductSerializers
from user.models import Group, User


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    model = Product
