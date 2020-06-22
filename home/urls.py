from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    path('', views.index,name="home"),
    path('login',views.loginUser,name="login"), 
    path('logout',views.logoutUser,name="logout"),
    path('signup',views.signup,name="signup"),
    path('user',views.userprofile,name="user"),    
    path('contact',views.contact,name="contact"),
    path('changeprofilephoto',views.photo,name="photo")

]
