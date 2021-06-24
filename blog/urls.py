from blog import views
from os import name
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
 
urlpatterns = [
    path("",views.index,name="index"),
    path("group/<int:id>/",views.group,name="group"),
    path("create_group/",views.create_group,name="create_group"),
    path("group_form/",views.group_form,name="group_form"),
    path("update_group/<int:id>",views.update_group,name="update_group"),

    path("loginUser/",views.loginUser,name="loginUser"),
    path("logoutUser/",views.logoutUser,name="logoutUser"),
    path("signUp/",views.signUp,name="signUp"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)