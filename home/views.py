from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from werkzeug.utils import secure_filename
import os
from django.contrib.auth import logout,login,authenticate
from datetime import datetime
from home.models import Contact
from home.models import Photo
from home.models import Post
from django.contrib import messages
# test user : SaifKhalid21
# password: saifkhalid
# Create your views here.
def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        lname=request.POST.get('lname')
        user = User.objects.create_user(username, email, password)
        user.last_name=lname
        # user.profilephoto=profilephoto
        user.save()
        return redirect('/')
    return render(request,'signup.html')

def index(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request,'index.html',context)

def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        # string=username+".jpg"
        if user is not None:
            login(request,user)
            return redirect('/user')
        else:
            return render(request,'login.html')
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')

def userprofile(request):
    return render(request,'user.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,'Done')
    return render(request,"contact.html")

def photo(request):
    if request.method=='POST':
        f=request.FILES['uploadfile']
        dp=Photo(img_file=f)
        dp.save()
        # f=str(f)
        return HttpResponse("UPLOADED SUCCESSFULLY.")
    return render(request,"profilephoto.html")
