from django.shortcuts import render
from djazango.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")