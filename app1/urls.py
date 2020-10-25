from django.urls import path
from . import views
urlpatterns = [
   
    path('', views.index),
    path('login/', views.login),
    path('adminlogin/', views.adminLogin),
    path('userdashboard/', views.userDashboard),
    path('dashboard/', views.dashboard),
    path('register/', views.register),
    path('Category/', views.Categorys),
    path('schemeadd/', views.schemeadd),
    path('users/', views.users),
    path('wardmember/', views.wardmember),
    path('edit/', views.edit),
    path('create/', views.create)

  
]
