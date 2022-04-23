from telnetlib import STATUS
from time import time
from django.db import models

# Create your models here.

class signup(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    dpimg = models.FileField(upload_to='app1/media',default="")

class NewPosts(models.Model):
    imageFile = models.FileField(upload_to='app1/media')
    upd_date = models.CharField(max_length=10)
    upd_time = models.CharField(max_length=10)
    user = models.ForeignKey(signup, on_delete = models.CASCADE,default='')
    like_counts = models.IntegerField()


class friends(models.Model):
    following = models.ForeignKey(signup, on_delete= models.CASCADE,related_name='following')
    followes = models.ForeignKey(signup, on_delete= models.CASCADE,related_name='follower')


class Comments(models.Model):
    cmnt = models.SlugField(max_length=100)
    c_date = models.CharField(max_length=10)
    c_time = models.CharField(max_length=10)
    c_fkey = models.ForeignKey(signup, on_delete= models.CASCADE,default='')
    c_imgkey = models.ForeignKey(NewPosts, on_delete= models.CASCADE,default='')


class Like(models.Model):
    like_user = models.ForeignKey(signup, on_delete= models.CASCADE,default='')
    img_key = models.ForeignKey(NewPosts, on_delete= models.CASCADE,default='')
    like_date = models.CharField(max_length=10)
    like_time = models.CharField(max_length=10)


class inbox(models.Model):
   
    sender = models.ForeignKey(signup,null=True, on_delete= models.CASCADE,related_name='user1')
    receiver = models.ForeignKey(signup,null=True, on_delete= models.CASCADE,related_name='user2')
    msg = models.CharField(max_length=500)
    addtime = models.CharField(max_length=10)
    adddate = models.CharField(max_length=10) 

    
    

     

    
        