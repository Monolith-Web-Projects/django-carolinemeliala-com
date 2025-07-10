from django.shortcuts import render
from .models import Product, Slide
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
import json


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


@csrf_exempt
def all_slides(request):
    slides = Slide.objects.all()
    data = {"fashion": [], "commercial": [], "editorial": []}
    for slide in slides:
        category = slide.category.name.lower()
        if category in data:
            data[category].append(slide.image_path)
    return JsonResponse(data)
