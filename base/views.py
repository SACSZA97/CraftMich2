from django.shortcuts import render
from .models import Articulos

# Create your views here.
def Carrusel(request):
    articulos=Articulos.objects.all()
    return render(request,"base/Carrusel.html", {'articulos':articulos})
