from django.urls import path,include
from .import views

urlpatterns =[
    path('log',views.logFn,name='log'),
    path('signup',views.sinFn,name='signup'),

]