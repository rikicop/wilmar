from django.shortcuts import render
from .models import Product

def home(request):
    prod = Product.objects.all()
    context = {'prod':prod}
    return render(request, 'home.html', context)

def product(request, pk):
    prod = Product.objects.get(id=pk)
    #context = {'prod':prod}
    return render(request, 'detalle.html', {'prod':prod})