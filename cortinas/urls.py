from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('detalle/<str:pk>', views.product,name='detalle'),
    path('tabla/',views.tabla, name='tabla'),
    path('videos/',views.videos, name='videos'),
    path('download_file/',views.download_file, name='download_file')
]
