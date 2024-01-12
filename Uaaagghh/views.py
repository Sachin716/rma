from django.shortcuts import render , redirect , HttpResponse
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User 
from .models import *
import random

def home(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        num = request.POST.get("Number")
        email = request.POST.get("Email")
        if email:
            form = Appointment(Name=name , Ph=num)
        else:
            form = Appointment(Name=name , Ph=num , Email = email)
        form.save()
        return redirect("/Confirmed")


    else:
        lis = list(review.objects.all())
        a1 = random.choice(lis)
        cat = reversed(services_cateogaries.objects.all())
        cat2 = reversed(services_cateogaries.objects.all()[:6])
        return render(request,"home.html" ,
        {
            "cate" : cat,
            "review":a1,
            "cate2":cat2
        })

def contacts(request):
    return render(request,"contacts.html")

def servicess(request,id):
    ser = services.objects.get(pk=id)
    if request.method == "POST":
        name = request.POST.get("Name")
        num = request.POST.get("Number")
        address = request.POST.get("address")
        book = services.objects.get(pk=id)
        cat = services.objects.get(pk=id).cate
        price = services.objects.get(pk=id).price
        if not address:
            form = Appointment(Name=name , Ph=num)
        else:
            messages.success(request,"thanks")
            form = Bookins(Client_Name=name, price=price, cateogary=cat,Book=book , client_number=num , Address = address)
        form.save()
        return redirect("/Confirmed")
    else:
        lis = list(review.objects.all())
        a1 = random.choice(lis)
        return render(request,"service.html",{"ser":ser , "review":a1} )


def appoint(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        num = request.POST.get("Number")
        email = request.POST.get("Email")
        if not email:
            form = Appointment(Name=name , Ph=num)
        else:
            form = Appointment(Name=name , Ph=num , Email = email)
        form.save()
        messages.success(request,("thanks"))
        return redirect("/Confirmed")
    else:
        lis = list(review.objects.all())
        a1 = random.choice(lis)
        return render(request,"appointment.html",{"review":a1})

def admin(request):
    if request.user.is_authenticated:
        return redirect("/admin_home")
    else:
        if request.method == "POST":
            uname = request.POST.get("uname")
            pas = request.POST.get("psw")
            use = authenticate(username=uname , password=pas)
            login(request,use)
            return redirect("/admin_home")
    return render(request,"admin_login.html")

def view(request):
    return render(request,"view.html")
# Create your views here.

def register(request):
    if  not request.user.is_authenticated:
        messages.success(request,"You must login to ur account to Create another Admin account")
        return redirect("/admin_login")
    if request.method == "POST":
        usname = request.POST.get("uname")
        if User.objects.filter(username=usname).exists():
            messages.success(request,"Username Already Taken")
            return redirect("/register")
        else:
            naaam = request.POST.get("Name")
            pas = request.POST.get("psw")
            cpas = request.POST.get("pswrep")
            form = User.objects.create_superuser(username=usname , password = pas , first_name = naaam)
            form.save()
            messages.success(request,"User created Successfully")
            return redirect("/admin_login")
    
    return render(request,'register.html')

def service_adder(request):
    return render(request,'add_service.html')

def admin_home(request):
    if request.user.is_authenticated:
        booking = reversed(Bookins.objects.all())
        app = Appointment.objects.all()
        return render(request,'Admin_home.html',{
            "book":booking,
            "ap":app
        })
    else:
        messages.success(request,"You Must Login to access the admin panel")
        return redirect("/admin_login")

def cat_page(request,cats):
    lis = list(review.objects.all())
    a1 = random.choice(lis)
    a = services_cateogaries.objects.get(cateogary=cats)
    servicesa = services.objects.filter(cate=a)
    if request.method=="POST":
        name = request.POST.get("Name")
        num = request.POST.get("Number")
        form = Appointment(Name=name , Ph=num)
        form.save()
    return render(request,"Services.html",{
        "ser":servicesa,
        "cat":a,
        "review":a1
    })

def conf(request):
    lis = list(review.objects.all())
    a1 = random.choice(lis)
    return render(request,"Booking_Confirmed.html",{"review":a1})


def checked(request,id):
    if request.user.is_authenticated:
        form = Bookins.objects.get(pk=id)
        form.checked = True
        form.save()
        return redirect("/admin_home")

    else:
        if request.method == "POST":
            ip = request.POST.get("IP")
            form = IP(Ip=ip)
            form.save()
            messages.success(request,"You cannot do that you ip have been recorded")
            return redirect("/admin_login")
        else:
            return render(request,"fetchIp.html")
        
def logoutt(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("/admin_login")
    else:
        messages.success(request,"You are not logged in in First Place")
        return redirect("/admin_login")


def galle(request):
    obj = reversed(gall.objects.all())
    lis = list(review.objects.all())
    a1 = random.choice(lis)
    return render(request,"gallery.html" , { "gall":obj , "review":a1})

def reviewsss(request):
    if request.method=="POST":
        name = request.POST.get("name")
        rev = request.POST.get("review")
        form = review(Name=name , review = rev)
        form.save()
        return redirect("/")
    else:
        return render(request,"review.html")