from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def index(request):
    return render(request, 'test.html') 


def Adminarea(parameter_list):
    """
    docstring
    """
    pass