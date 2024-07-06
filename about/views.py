from django.shortcuts import render
from .models import About
# Create your views here.
def about(request):
    about_info = About.objects.all()
    return render(request, 'about/about.html', {'about_info': about_info})