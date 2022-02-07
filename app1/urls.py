from unicodedata import name
from django.urls import path,include
from .import views

urlpatterns =[
    path('',views.log_in,name='login'),
    path('signup',views.sign_up,name='signup'),
    path('home',views.home_page,name='home'),
    path('inbox',views.inbox_page,name='inbox'),
    path('notification',views.notifications,name='notification'),
    path('profile',views.profile_page,name='profile'),
    path('viewtb',views.user_table,name='viewtb'),
    path('deletetb/<int:id>',views.delete_user,name='deletetb'),
    path('session',views.sessionFn,name='session'),
    path('logout',views.log_out,name='logout'),
    path('ajax',views.ajaxFn,name='ajax')

]