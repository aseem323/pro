from django.urls import path,include
from .import views

urlpatterns =[
    path('log',views.logFn,name='log'),
    path('signup',views.sinpfn,name='signup'),
    path('home',views.homefn,name='home'),
    path('inbox',views.inboxfn,name='inbox'),
    path('notification',views.notfn,name='notification')

]