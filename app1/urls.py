from unicodedata import name
from django.urls import path,include
from .import views

urlpatterns =[
    path('login',views.LogIn,name='login'),
    path('signup',views.SignUp,name='signup'),
    path('home',views.home_page,name='home'),
    path('inbox',views.inbox_page,name='inbox'),
    path('notification',views.notifications,name='notification'),
    path('profile',views.profile_page,name='profile'),
    path('logout',views.LogOut,name='logout'),
    path('ajax_username',views.AjaxUsername,name='ajax_username'),
    path('ajax_email',views.AjaxEmail,name='ajax_email'),
    path('search',views.search_user,name='search'),
    path('new_post',views.newposts,name='new_post'),
    path('edit/<int:id>',views.edit_user,name='edit'),
    path('update/<int:id>',views.update_user,name='update'),
    path('follow',views.followFn,name='follow'),
    path('change_pass',views.change_password,name='change_pass'),
    path('profile_view/<int:id>',views.ProfileView,name='profile_view'),
    path('comments/<int:id>',views.Comment,name='comments'),
    path('ajax_edit',views.AjaxEdit,name='ajax_edit'),
    path('add_dp',views.add_dpFn,name='add_dp'),
    path('likes',views.Likes,name='likes'),
    path('delete_post/<int:id>',views.DeletePost,name='delete_post'),
    path('search_users',views.SearchUser,name='search_users'),
    path('msguser/<int:id>',views.MsgUser,name='msguser'),
    path('message/<int:id>',views.Message,name='message')
    
    

    


    # path('unfollow/<int:id>',views.unfollowFn,name='unfollow'),
    # path(r'^unfollowfn/(?P<backend>\w+?)/$', views.unfollowFn,name='unfollowfn')
    
    

]