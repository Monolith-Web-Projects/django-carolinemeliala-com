from django.shortcuts import render
from .models import Product
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse

@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({
        "detail": "CSRF cookie set",
        "csrfToken": request.META.get("CSRF_COOKIE")
    })


@csrf_exempt
def product_list(request):
    products = Product.objects.all()
    data = []
    for product in products:
        data.append({
            "productId": product.productId,
            "productCategory": product.productCategory,
            "productName": product.productName,
            "productColor": product.productColor,
            "productImage": product.productImage,
            "productSize": product.productSize,
            "productQuantity": product.productQuantity,
            "productDescription": product.productDescription,
            "productPrice": product.productPrice
        })
    return JsonResponse(data, safe=False)
