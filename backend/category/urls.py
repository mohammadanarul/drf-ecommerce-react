from unicodedata import name
from django.urls import path 
from .views import CategoryViewSet

urlpatterns = [
    path('list/', CategoryViewSet.as_view({'get': 'list'}))
]
