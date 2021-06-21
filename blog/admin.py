from blog.models import Belong, Blog, Group, Post
from django.contrib import admin

admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Group)
admin.site.register(Belong)
