from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from app1.models import *

def index(request):
    return render(request, 'index.html') 

def login(request):
    if request.method == 'POST':
        return render(request, 'user_dashboard.html')
    else:
        return render(request, 'login.html')
    
def userDashboard(request):
    return render(request,  'user_dashboard.html',)

def register(request):
    return render(request, 'register.html')

def adminLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password =  request.POST['password']
        if username == 'admin' and password == 'admin':
            request.session['username'] = username
            return redirect(dashboard)
        else:
            return render(request,  'adminlogin.html')
    else:
        return render(request,  'adminlogin.html')

def dashboard(request):
    return render(request,  'dashboard.html')

def Categorys(request):
    if request.method == 'POST':
        category1 = request.POST['category']
        student = Category.objects.create(category=category1)
        student.save()
       
        return render(request, 'Category.html')
    else:
        return render(request, 'Category.html')

def schemeadd(request):
    list = Category.objects.all()
    return render(request, 'schemeadd.html',{'data':list}) 
    if request.method == 'POST':
        scheme = request.POST['scheme']
        dop = request.POST['dop']
        vld = request.POST['validdate']
        cat = request.POST['category']
        scheme = scheme.objects.create(schemename=scheme,datepub=dop,validdate=vld,category=cat)
        scheme.save()
        return render(request, 'Category.html')
    else:
        return render(request, 'Category.html')

def users(request):
    list = Scheme.objects.all()
    return render(request, 'Users.html',{'data':list})

def wardmember(request):
    return render(request, 'Wardmember.html')

def edit(request):
    return render(request, 'Update.html')


def create(request):
    return render(request, 'Create.html')