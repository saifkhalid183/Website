from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate
from datetime import datetime
from home.models import Contact
from home.models import Photo
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
        user.profilephoto=profilephoto
        user.save()
        return redirect('/')
    return render(request,'signup.html')

def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'index.html')

def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
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
    if request.method=="POST":
        img_file=request.POST.get('img_file')
        profilephoto=Photo(img_file=img_file)
        profilephoto.save()
    return render(request,"profilephoto.html")