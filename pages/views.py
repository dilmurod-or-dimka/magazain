from django.shortcuts import render, HttpResponse
from .models import Product, Category


# Create your views here.

def home_view(request):
    products = Product.objects.all()[:9]
    context = {
        "products": products
    }
    return render(request, "pages/index.html", context)


def shop_view(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "pages/shop.html", context)


def category_products(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    context = {
        "products": products
    }
    return render(request, "pages/shop.html", context)


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        "product": product
    }
    return render(request, "pages/product_detail.html", context)
