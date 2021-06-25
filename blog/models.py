from contextlib import nullcontext
from django.db import models
from django.db.models.aggregates import Aggregate
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from django.utils import timezone


class Group(models.Model):
    name=models.CharField(max_length=70,null=False)
    img=models.ImageField(blank=True,null=True)
    disc=models.TextField(null=False)
    creater=models.ForeignKey(User,on_delete=models.CASCADE,null=False)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=70,null=False)
    disc=models.TextField(blank=True,null=True)
    img=models.ImageField(blank=True,null=True)
    file=models.FileField(upload_to ='uploads_blog/',blank=True,null=True)
    creater=models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    group=models.ForeignKey(Group,on_delete=models.CASCADE,null=False)
    date=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    post=models.TextField()
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,null=False) 
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    img=models.ImageField(blank=True,null=True)
    file=models.FileField(upload_to ='uploads_post/',null=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post

class Belong(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    group=models.ForeignKey(Group,on_delete=models.CASCADE,null=False)

    def __str__(self):
        return str(self.user)