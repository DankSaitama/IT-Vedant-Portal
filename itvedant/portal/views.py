from django.shortcuts import render,redirect
from django.urls import path

# Create your views here.

def index(request):
    return render(request,'index.html')

#UserAuthentication
from .forms import RegisterForm

def register_page(request):
    form=RegisterForm()
    context = {
        "title":"Registration Page",
        "form":form
    }

    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=True)
            user.set_password(user.password)
            user.save()
            return redirect('/base')
        else:
            return render(request,"register.html",context)
    return render(request,"register.html",context)


#UserLogin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

def login_page(request):
    loginform=AuthenticationForm()
    if request.method=="POST":
        username=request.POST.get('username')
        pwd=request.POST.get('password')
        print(username,pwd)
        user=authenticate(username=username,password=pwd)
        print(user)
        if user!=None:
            
            login(request,user)
            print(request,user)
            return redirect("/home")
        else:
            msg='Invalid username or password'
            return render(request,'login.html',{'form':loginform,'msg':msg})
    return render(request,'login.html',{'form':loginform})

#UserLogout
from django.contrib.auth import authenticate, logout

def logout_page(request):
    print(request.user)
    logout(request)
    print(request.user)
    return redirect('/login')

#Home
def Homepage(request):
    return render(request,'Home.html')

