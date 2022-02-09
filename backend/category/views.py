from rest_framework import viewsets, generics
from .serializers import CategorySerializer
from .models import Category

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.root_nodes()
    serializer_class = CategorySerializer
