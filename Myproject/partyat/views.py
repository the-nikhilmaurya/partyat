from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import Venues
from partyat import forms
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"partyat/index.html",)


def SignUpPage(request):
    if request.method == 'POST':
        user_name = request.POST.get("user_name")
        name=request.POST.get("name")
        email_id = request.POST.get("email_id")
        pass1 = request.POST.get("pass1")
        pass2= request.POST.get("pass2")
        if pass1 == pass2:
            new_user = User.objects.create_user(user_name,email_id,pass1,first_name=name.split()[0],last_name=name.split()[1])
            new_user.save()
            return redirect('login')
            # return HttpResponse("user created ")
        else:
            return HttpResponse("password did't match")
        # print(user_name,email_id,pass1,pass2)

    return render(request,"partyat/SignUpPage.html")


def LogInPage(request):
    if request.method== 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('HomePage')
        else:
            return HttpResponse("email id or password is incorrect")
        # print(email_id,password)

    return render(request,"partyat/LogInPage.html")


def ForgotPassword(request):
    return render(request,'partyat/forgotPassword.html')


def HomePage(request):
    return render(request,"partyat/HomePage.html")


def BookingTable(request):
    if request.method == 'POST':
        venue_name=request.POST.get('venue_name')
        name=request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        date= request.POST.get("date")
        time= request.POST.get("time")
        
        
        
        if Venues.objects.filter(venue_name=venue_name,date=date,time=time):
            messages.success(request,"booked success")
            return redirect ("HomePage")
            # return HttpResponse("success")

        else:
            messages.error(request,"invalid credentials")
            return redirect('BookingTable')
            return HttpResponse("not done")
    
        
        #emails starts from here
      
    return render(request,"partyat/bookingPage.html")