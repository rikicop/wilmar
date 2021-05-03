from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Post
import mimetypes
import json

import pandas as pd

def home(request):
    prod = Post.objects.all()
    context = {'prod':prod}
    return render(request, 'home.html', context)

def product(request, pk):
    prod = Post.objects.get(id=pk)
    #context = {'prod':prod}
    return render(request, 'detalle.html', {'prod':prod})


def tabla(request):
    prod = Product.objects.all()
    df = pd.DataFrame(list(Product.objects.all().values()))
    df.to_csv(r'media/precios.csv')
    #context = {'prod':prod}
    
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'tabla.html', context)

def download_file(request):
  
    fl_path = 'media/precios.csv'
    filename = 'precios.csv'

    fl = open(fl_path, 'rb')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response