from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as logouts
from django.contrib.auth.decorators import login_required
from home.models import Contact
# Create your views here.
@login_required(login_url="login")
def dashboard(request):
    return render(request,"dashboard.html")
def index(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get('email')
        job=request.POST.get("job")
        message=request.POST.get("message")
        contact=Contact(name=name,email=email,designation=job,message=message)
        contact.save()
        messages.success(request,"You message added successfully")
        return redirect('index')

    return render(request,"index.html")
def signup(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirmpass=request.POST.get("cnf_password")
        if(password!=confirmpass):
            messages.error(request, "Password not matched please re-enter passwords")
        else:
            user=User.objects.create_user(uname,email,password)
            user.save()
            return redirect("login")

    return render(request,"signup.html")
def Login(request):
   
    if request.method=="POST":
        uname=request.POST.get("uname")
        password=request.POST.get("password")
        user=authenticate(request,username=uname,password=password)
        if user is not None:
            login(request,user)
            return redirect("dashboard")
        else:
            return HttpResponse("Invalid username or password")

    return render(request,"login.html")

def logout(request):
    logouts(request)
    return redirect("main")

def farmDash(request):
    return render(request,"farmDash.html")