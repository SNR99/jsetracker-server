from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse


def home(request):
    return HttpResponse("<h1>API server is running</h1>")
