from django.shortcuts import render
from .models import cnscl


# Create your views here.
def index(request):
    anss = cnscl.objects.all()
    return render(request, "index.html", {'anss': anss})
