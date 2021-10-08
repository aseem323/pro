from django.shortcuts import render

# Create your views here.
def logFn(request):
    return render(request,'log.html')

    