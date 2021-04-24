from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import mimetypes

def home(request):
    prod = Product.objects.all()
    context = {'prod':prod}
    return render(request, 'home.html', context)

def product(request, pk):
    prod = Product.objects.get(id=pk)
    #context = {'prod':prod}
    return render(request, 'detalle.html', {'prod':prod})

def download_file(request):
  
    fl_path = 'wilmar_project/media/historical.xlsx'
    filename = 'historical.xlsx'

    fl = open(fl_path, 'rb')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response