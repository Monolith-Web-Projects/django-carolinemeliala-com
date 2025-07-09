from django.urls import path
from .views import get_csrf_token, product_list


urlpatterns = [
    path('get-token/', get_csrf_token),
    path('products/', product_list),
]