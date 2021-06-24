from .form import *
from django import forms
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
    context={"group_list":group_list}
    return render(request,"blog/index.html",context)

def group(request,id):
    group=Group.objects.get(id=id)
    members=Belong.objects.filter(group=id)
    # print(members)
    form=GroupForm(instance=group)
    # print(group.disc)
    

    context={"group":group,"members":members,"form":form,"id":id}
    return render(request,"blog/group.html",context)

def group_form(request):
    form=GroupForm()
    context={"form":form}
    return render(request,"blog/group_form.html",context)

def create_group(request):
    if request.method=="POST":
        form=GroupForm(request.POST)
        if form.is_valid():
            
            messages.success(request,"Form submittd Successfully")
            group=form.save()

            belong=Belong(user=request.user,group=group)
            belong.save()
            return redirect("/")
        else:
            messages.error(request,"Form is not Valid")
            return redirect("/group_form")

def update_group(request,id):
    groups=Group.objects.get(id=id)
    admin=Group.objects.get(id=id).creater
    if request.method=="POST":
        form=GroupForm(request.POST,instance=groups)
        if form.is_valid():
            if admin==request.user:
                messages.success(request,"Group Updated")
                group=form.save()
            else:
                messages.error(request,"You are not admin")
            return redirect("/")
        else:
            messages.error(request,"Form is not valid")
            return redirect("/group/id")

def delete_group(request,id):
    groups=Group.objects.get(id=id)
    if request.method=="POST":
        groups.delete()
        return redirect("/")

def all_groups(request):
    groups=Group.objects.all()
    context={"groups":groups}
    return render(request,"blog/all_groups.html",context)





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