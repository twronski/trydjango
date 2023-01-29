from django.shortcuts import render
from .models import Product


def products_view(request, *args, **kwargs):
	return render(request, 'products.html', {})
# Create your views here.

def product_detail_view(request, *args, **kwargs):
	obj = Product.objects.get(id=1)
	context = {'obj1' : obj}
	return render(request, 'product/product.html', context)

