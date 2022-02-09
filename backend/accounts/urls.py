from django.urls import path
from .views import (
    user_list_api,
    user_register_api,
    user_login_api,
)

urlpatterns = [
    path('user-list/', user_list_api),
    path('user-register/', user_register_api),
    path('login/', user_login_api),
]
