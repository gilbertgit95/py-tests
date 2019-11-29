from django.shortcuts import render
from . import models

# Create your views here.
from django.http import HttpResponse


def home(request):
    products = models.Product.objects.all()

    return render(request, 'products/products_list.html', {'products': products})

def product(request):
    product_id = request.GET.get('id', '')
    if len(product_id):
        product = models.Product.objects.filter(id=product_id)[0]

    return render(request, 'products/product.html', {'product': product})

def polls(request):
    return HttpResponse("Hello, world. You're at the polls index.")
