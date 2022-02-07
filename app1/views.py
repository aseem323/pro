import email
from email import message
from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import redirect, render

from app1.models import signup

# Create your views here.
def log_in(request):
    if request.method=="POST":
        username1 = request.POST['username']
        password1 = request.POST['password']
        try:
            log_query = signup.objects.get(username=username1)
            if((log_query.username == username1) and (log_query.password == password1)):
                request.session['user_log']=log_query.id
                return redirect('session')
            else:
                return render(request,'log.html',{'error':'incorrect password'})

        except:
            return render(request,'log.html',{'error':'incorrect username'})
    return render(request,'log.html')


def sessionFn(request):
    if 'user_log' in request.session:
        return render(request,'home.html')
    else:
        return render(request,'log')

def log_out(request):
    del request.session['user_log']
    return redirect('log')


def sign_up(request):
    if request.method =="POST":
        #print('hiiiiii')
        sname = request.POST['fname']
        semail = request.POST['femail']
        suname = request.POST['fusername']
        spass = request.POST['fpassword']
        reg_data = signup(name=sname,email=semail,username=suname,password=spass)
        reg_data.save()
        
    return render(request,'signup.html')

def ajaxFn(request):
    # print('hiiiiiiii')
    aj = request.POST['username']
    #print(aj)
    #obj = signup.objects.filter(username=aj).exists()
    #print(obj)
    try:
        signup.objects.get(username=aj)
        return JsonResponse({'message':True})
        # if obj.username==aj:
        # else:
        #     return JsonResponse({'message':False})
    except:
        return JsonResponse({'message':False})
        

def user_table(request):
    getdata = signup.objects.all()
    return render(request,'table.html',{'data':getdata})

def delete_user(request,id):
    signup.objects.get(id=id).delete()
    return redirect('viewtb')
    #return render(request,'table.html')


def home_page(request):
    return render(request,'home.html')

def inbox_page(request):
    return render(request,'inbox.html')

def notifications(request):
    return render(request,'notific.html')

def profile_page(request):
    return render(request,'profile.html')