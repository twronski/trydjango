from django.shortcuts import render
from .models import Product


def products_view(request, *args, **kwargs):
	return render(request, 'products/products.html', {})
# Create your views here.

def product_detail_view(request, *args, **kwargs):
	obj = Product.objects.get(id=1)
	context = {'obj1' : obj}
	return render(request, 'products/product_detail.html', context)

def product_create_view(request, *args, **kwargs):
	context = {}
	return render(request, 'products/product_create.html', context)

