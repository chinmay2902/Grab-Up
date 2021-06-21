from blog.models import Post
from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def index(request):
    user=User.objects.get(username=request.user.username)
    belong=Belong.objects.filter(user=user)
    group_list=[]
    for b in belong:
        group_list.append(b.group)
    # print(group_list)
    context={"group_list":group_list}
    return render(request,"blog/index.html",context)

def group(request,id):
    groups=Group.objects.filter(id=id)
    members=Belong.objects.filter(group=id)
    # print(members)
    context={"groups":groups,"members":members}
    return render(request,"blog/group.html",context)

def loginUser(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.error(request,"Login Failed")
            return render(request,"auth/loginUser.html")
    return render(request,"auth/loginUser.html")

def logoutUser(request):
    logout(request)
    return redirect("loginUser")

def signUp(request):
    if request.method=="POST":
        username=request.POST.get("username")
        pass1=request.POST.get("pass1")
        pass2=request.POST.get("pass2")
        if pass1==pass2:
           add=User.objects.create_user(username=username,password=pass1)
           add.save()
           messages.success(request,"User Added Successfully")
           return redirect("loginUser")
        else:
            messages.error(request,"Invalid Input")
            return render(request,"auth/signUp.html")
    return render(request,"auth/signUp.html")