from multiprocessing import context
from pdb import post_mortem
from django.shortcuts import render , HttpResponse
from datetime import datetime
from EDtechapp.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,"index.html")

def About(request):
    return render(request,"about.html")

def Courses(request):
    return render(request,"course.html")

def Contact(request):
    if request.method== "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        Contact = Contact(name=name, email=email,phone=phone,desc=desc,date=datetime.today())
        Contact.save()
        messages.success(request,'your messages has been sent!')

    return render(request,"contact.html")   

def Login(request):
    return render(request,"Login.html")