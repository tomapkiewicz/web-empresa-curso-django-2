from django.shortcuts import render
from .models import Service


# Create your views here.
def servicios(request):
    servicios = Service.objects.all()
    return render(request, "service/services.html", {'servicios': servicios})
