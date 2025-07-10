from django.urls import path
from .views import get_csrf_token, product_list, all_slides


urlpatterns = [
    path('get-token/', get_csrf_token),
    path('products/', product_list),
    path('slides/', all_slides),
]