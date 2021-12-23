from django.shortcuts import render

# Create your views here.
def logFn(request):
    return render(request,'log.html')

def sinpfn(request):
    return render(request,'signup.html')

def homefn(request):
    return render(request,'home.html')

def inboxfn(request):
    return render(request,'inbox.html')

def notfn(request):
    return render(request,'notific.html')