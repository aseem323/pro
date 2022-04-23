from django.shortcuts import redirect, render
from app1.models import signup


def AdminLogin(request):
    uname = 'haseem'
    upassword = 12345
    if request.method=="POST":
        ad_name = request.POST['name']
        ad_password = request.POST['password']

        try: 
            data = uname == ad_name
            if  ad_name==uname and int(ad_password)==upassword:
                return redirect ('adminhome')
            else:
                return render (request,'admin_login.html',{"error":"invalid name or password"})
        except:
            return render (request,'admin_login.html',{"error":"invalid name or password"})

    return render (request,'admin_login.html')



def AdminLogout(request):
    
    return redirect('adminlogin')



def AdminHome(request):
    userdata = signup.objects.all()

    return render (request,'user_table.html',{'data':userdata})



def DeleteUser(requset,id):
    signup.objects.filter(id=id).delete()

    return redirect('adminhome')