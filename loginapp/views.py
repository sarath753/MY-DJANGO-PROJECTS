from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def loginfunc(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username = username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.success(request,("There was an error logging in please enter the valid login details"))
            return render(request,"login/loginform.html")
    return render(request,"login/loginform.html")

def home(request):
    return render(request,"login/home.html")


