from django.shortcuts import render
from .models import NavbarItem
# Create your views here.
def home(request):
    navbar_items = NavbarItem.objects.all()
    return render(request, 'home/home.html', {'navbar_items': navbar_items})

def about(request):
    navbar_items = NavbarItem.objects.all()
    return render(request, 'about/about.html', {'navbar_items': navbar_items})

def services(request):
    navbar_items = NavbarItem.objects.all()
    return render(request, 'services/services.html', {'navbar_items': navbar_items})