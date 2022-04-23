from unicodedata import name
from django.urls import path,include
from .import views

urlpatterns = [
    path('adminlogin',views.AdminLogin,name='adminlogin'),
    path('adminhome',views.AdminHome,name='adminhome'),
    path('delete_user/<int:id>',views.DeleteUser,name='delete_user'),
    path('adminlogout',views.AdminLogout,name='adminlogout')

]