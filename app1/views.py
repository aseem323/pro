from datetime import datetime
import email
from email import message
from importlib.metadata import files
import random
from this import d
from unicodedata import name
from xmlrpc.client import DateTime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from random import random
from app1.models import Comments, Like, friends, inbox, signup
from django.core.files.storage import FileSystemStorage
from app1.models import NewPosts
from django.db.models import Q
from django.db.models.sql.query import Query

# Create your views here.       
def LogIn(request):
    if request.method == "POST":
        username1 = request.POST['username']
        password1 = request.POST['password']

        try:
            log_query = signup.objects.get(username=username1)
            if((log_query.username == username1) and (log_query.password == password1)):
                request.session['user_log']=log_query.id
                return redirect('home')
            else:
                return render(request,'login.html',{'error':'Sorry, your password was incorrect'})

        except:
            return render(request,'login.html',{'error':"Please check your username and try again"})

    return render(request,'login.html')



# def sessionFn(request):
#     if 'user_log' in request.session:
#         return render(request,'home.html')
#     else:
#         return render(request,'login')



def LogOut(request):
    del request.session['user_log']

    return redirect('login')



def SignUp(request):
    if request.method == "POST":
        sname = request.POST['fname']
        semail = request.POST['femail']
        suname = request.POST['fusername']
        spass = request.POST['fpassword']
        reg_data = signup(name=sname,email=semail,username=suname,password=spass)
        reg_data.save()

        return redirect ('login')

    return render(request,'signup.html')



def AjaxUsername(request):
    aj = request.POST['username']
    
    try:
        signup.objects.get(username=aj)
        return JsonResponse({'message':True})

    except:
        return JsonResponse({'message':False})



def AjaxEmail(request):
    aj2 = request.POST['email']

    try:
        signup.objects.get(email=aj2)
        return JsonResponse({'message':True})

    except:
        return JsonResponse({'message':False})

    

def edit_user(request,id):
    edit_data = signup.objects.get(id=request.session['user_log'])

    return render(request,'edit.html',{"editdata":edit_data,'id':id})



def update_user(request,id):
    if request.method == "POST":
        ename = request.POST['fname']
        eemail = request.POST['femail'] 
        eusername = request.POST['fusername'] 
        signup.objects.filter(id=request.session['user_log']).update(name=ename,email=eemail,username=eusername)

        return redirect('profile')

    return redirect('edit',id)



def AjaxEdit(request):
    ajax = request.POST['username']
    
    try:
        signup.objects.get(username=ajax)
        return JsonResponse({'msg':True})
         
    except:
        return JsonResponse({'msg':False})



def change_password(request):
    if request.method == "POST":
        oldpassword = request.POST['oldpass']
        newpassword = request.POST['newpass']
        confpassword = request.POST['confpass']
        passdata = signup.objects.get(id=request.session['user_log'])

        if passdata.password == oldpassword:
            passdata.password = newpassword
             
            if newpassword == confpassword:
                passdata.save()
                return redirect('profile')
            else:
                return render(request,'pass.html',{"perror":"password does't mach"})

        else:
            return render(request,'pass.html',{"error":"inavlid password"})

    return render(request,'pass.html')



def home_page(request):
    # if 'user_log' in request.session:
    #     return redirect('home')
    mypost = NewPosts.objects.filter(user=request.session['user_log'])

    post = []
    getdata = friends.objects.filter(followes=request.session['user_log'])

    for i in getdata:
        posts = NewPosts.objects.filter(user=i.following)

        for j in posts: 
            if Like.objects.filter(like_user_id=request.session['user_log'], img_key_id=j.id).exists():
                newPostObj = {
                    "id":j.id,
                    "imageFile":j.imageFile,
                    "upd_date":j.upd_date,
                    "upd_time":j.upd_time,
                    "user":j.user,
                    "like_count":j.like_counts,
                    "like": True 
                }
            else:
                newPostObj = {
                    "id":j.id,
                    "imageFile":j.imageFile,
                    "upd_date":j.upd_date,
                    "upd_time":j.upd_time,
                    "user":j.user,
                    "like": False 
                }

            post.append(newPostObj) 

    return render(request,'home.html',{'data':post,'mydata':mypost})



def SearchUser(requset):
    if requset.method == "POST":
        searchdata = requset.POST['search']
        obj = signup.objects.filter(Q(username__icontains=searchdata))

        return render(requset,'select_msg.html',{"data":obj,})

    return redirect('inbox')



def MsgUser(request,id):
    obj = signup.objects.get(id=id)
    received_msg = inbox.objects.filter(receiver=request.session['user_log'],sender=obj)
    sent_message = inbox.objects.filter(sender=request.session['user_log'],receiver=obj)

    return render (request,'message.html',{'data':obj,'rec_msg':received_msg,'sent_msg':sent_message})



def inbox_page(request):
    msgs = inbox.objects.filter(receiver=request.session['user_log']).distinct('receiver_id','sender_id')

    return render(request,'inbox.html',{"data":msgs})



def Message(request,id):
    if request.method == "POST":
        sent_date = datetime.now().strftime('%d/%m/%Y')
        sent_time = datetime.now().strftime("%I:%M %p")
        msg = request.POST['messages']
        receiver = signup.objects.get(id=id)
        sender = signup.objects.get(id=request.session['user_log'])
        obj = inbox(sender=sender,receiver=receiver,msg=msg,addtime=sent_time,adddate=sent_date)
        obj.save()  

        return redirect('/msguser/'+str(id))

    return render (request,'message.html')



def newposts(request):
    if request.method == "POST":
        file = request.FILES['newpost']
        post_date = datetime.now().strftime('%d/%m/%Y')
        post_time = datetime.now().strftime("%I:%M %p")
        obj = NewPosts(imageFile=file,user_id=request.session['user_log'],upd_date=post_date,upd_time=post_time,like_counts=0)
        obj.save()

    return render(request,'post.html')



def notifications(request):
    obj = friends.objects.filter(following=request.session['user_log'])
    
    likedPosts = []
    posts = NewPosts.objects.filter(user=request.session['user_log'])

    for postObj in posts:
        likes = Like.objects.filter(img_key=postObj.id)

        for like in likes:
            likedPosts.append({
                'nameOfUser': like.like_user.name,
                'profilePic': like.like_user.dpimg.url,
                'postName': like.img_key.imageFile.url,
                'postdate': like.like_date,
                'posttime': like.like_time
            })

    commentpost = []
    c_post = NewPosts.objects.filter(user=request.session['user_log'])

    for d in c_post:
        comment = Comments.objects.filter(c_imgkey=d.id)

        for e in comment:
            commentpost.append({
                'name': e.c_fkey.name,
                'profile': e.c_fkey.dpimg.url,
                'pic':e.c_imgkey.imageFile.url,
                'postcmt': e.cmnt,
                'date': e.c_date,
                'time': e.c_time
            })

    return render(request,'notification.html',{"data": obj, "likedPosts": likedPosts,"comentdata":commentpost})
    


def profile_page(request):
    # obj = signup.objects.get(id=request.session['user_log'])
    post_count = NewPosts.objects.filter(user=request.session['user_log']).count()
    data = NewPosts.objects.filter(user=request.session['user_log'])
    objprofile = signup.objects.get(id=request.session['user_log'])
    follow_count = friends.objects.filter(followes=request.session['user_log']).count()
    followers_count = friends.objects.filter(following=request.session['user_log']).count()
    getdata = NewPosts.objects.select_related("user")

    return render(request,'profile.html',{"data":getdata,'posts':data,'count':post_count,'profile':objprofile,'following':follow_count,'followers':followers_count})



def DeletePost(request,id):
    NewPosts.objects.get(id=id).delete()

    return redirect('profile')



def add_dpFn(request):
    if request.method == "POST":
        dpfile = request.FILES['dpimage']
        obj = signup.objects.get(id=request.session['user_log'])
        obj.dpimg = dpfile
        obj.save()

        return redirect('profile')

    return render(request,'add.html')



def search_user(request):
    if request.method == "POST":
        search_data = request.POST['searchbox']
        obj = signup.objects.filter(Q(username__icontains=search_data))

        if obj:
            return render(request,'user.html',{"userdata":obj,})
        else:
            return render(request,'user.html',{'error':'no result found'})

    return redirect('profile')



def ProfileView(request,id):
    following = False
    already_following = friends.objects.filter(following=id,followes=request.session['user_log']).exists()

    if already_following:
        following = True
    obj = signup.objects.get(id=id)

    return render(request,'user_view.html',{"data":obj,'following':following})



def followFn(request):
    if request.method == "POST": 

        if 'following' in request.POST: 
            user_id = signup.objects.get(id=request.POST['user_id'])
            userid = signup.objects.get(id=request.session['user_log'])
            follow_data = friends(following=user_id,followes=userid,)
            follow_data.save()

        if 'unfollow' in request.POST:
            obj = friends.objects.get(following=request.POST['user_id'],followes=request.session['user_log'])
            obj.delete()

    return redirect ('home')



def Comment(request,id):
    if request.method == "POST":
        coments = request.POST['cmnts']
        img_id = NewPosts.objects.get(id=id)
        usr_id = signup.objects.get(id=request.session['user_log'])
        cmnt_date = datetime.now().strftime('%d/%m/%Y')
        cmnt_time = datetime.now().strftime("%I:%M %p")
        obj = Comments(cmnt=coments,c_fkey=usr_id,c_imgkey=img_id,c_date=cmnt_date,c_time=cmnt_time)
        obj.save()

    data = Comments.objects.filter(c_imgkey=id)
    
    return render(request,'comment.html',{'id':id,'cmt':data})
    


def Likes(request):
    if request.method=='POST':
        temp = request.POST['li_image']
        post=NewPosts.objects.get(id=temp)

        if 'like' in request.POST:
            user = request.session['user_log']
            date = datetime.now().strftime('%d/%m/%Y')
            time = datetime.now().strftime('%I:%M %p')
            post.like_counts+=1
            post.save()
            obj = Like(like_user_id=user,img_key_id=temp,like_date=date,like_time=time)
            obj.save()

        if 'unlike' in request.POST:
            temp = request.POST['li_image']
            user = request.session['user_log']
            obj2 = Like.objects.get(like_user_id=user,img_key_id=temp)
            obj2.delete()
            post.like_counts-=1
            post.save()
            
    return redirect('home')












































    # if request.method =="POST":
    #     if 'like' in request.POST:
    #         like =signup.objects.get(id=request.session['user_log'])
    #         l_image = NewPosts.objects.get(id=request.POST['image'])
    #         l_date=datetime.now().strftime('%d/%m/%Y')
    #         l_time=datetime.now().strftime("%I:%M %p")
    #         obj = Like(like_user=like,img_key=l_image,like_date=l_date,like_time=l_time)
    #         obj.save()
            
    #     if 'unlike' in request.POST:
    #         obj2 = Like.objects.get(like_user=request.session['user_log'],img_key=request.POST['li_image'])
    #         obj2.delete()

    #return redirect('home')


# def followFn(request):
#     obj = signup.objects.get(id=request.POST['following'])
#     obj2 = signup.objects.get(id=request.session['user_log'])
#     try:
#         follow_data = friends(following=obj,folloews=obj2)
#         follow_data.save()
#         return JsonResponse({'msg':True})
#     except:
#         return JsonResponse({'msg':False})


# def unfollowFn(request,id):
#     obj = signup.objects.get(id=id)
#     return render(request,'user_viewunfollow.html',{"data":obj})






