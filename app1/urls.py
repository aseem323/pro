from unicodedata import name
from django.urls import path,include
from .import views

urlpatterns =[
    path('log',views.logFn,name='log'),
    path('signup',views.sinpfn,name='signup'),
    path('home',views.homefn,name='home'),
    path('inbox',views.inboxfn,name='inbox'),
    path('notification',views.notfn,name='notification'),
    path('profile',views.profn,name='profile'),
    path('viewtb',views.tablefn,name='viewtb'),
    path('deltb/<int:id>',views.delfn,name='deltb'),
    path('session',views.sessionfn,name='session'),
    path('logout',views.logoutfn,name='logout'),
    path('aja',views.ajaxfn,name='aja')

]