from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404


# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')