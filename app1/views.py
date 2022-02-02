import email
from email import message
from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import redirect, render

from app1.models import signup

# Create your views here.
def logFn(request):
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


def sessionfn(request):
    if 'user_log' in request.session:
        return render(request,'home.html')
    else:
        return render(request,'log')

def logoutfn(request):
    del request.session['user_log']
    return redirect('log')


def sinpfn(request):
    if request.method =="POST":
        #print('hiiiiii')
        sname = request.POST['fname']
        semail = request.POST['femail']
        suname = request.POST['fusername']
        spass = request.POST['fpassword']
        reg_data = signup(name=sname,email=semail,username=suname,password=spass)
        reg_data.save()
        
    return render(request,'signup.html')

def ajaxfn(request):
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
        

def tablefn(request):
    getdata = signup.objects.all()
    return render(request,'table.html',{'data':getdata})

def delfn(request,id):
    signup.objects.get(id=id).delete()
    return redirect('viewtb')
    #return render(request,'table.html')


def homefn(request):
    return render(request,'home.html')

def inboxfn(request):
    return render(request,'inbox.html')

def notfn(request):
    return render(request,'notific.html')

def profn(request):
    return render(request,'profile.html')