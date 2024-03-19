from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .forms import *
from.models import *
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse


def hospitalregisterview(request):
    if request.method=='POST':
        u=hospitalregistermodel.objects.filter(username=request.POST['username'])
        if u.exists():
            messages.info(request,'user already exists')
            return redirect('myapp1:hospital')
        form=hospitalregisterform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myapp1:hospital')
    f=hospitalregisterform()
    return render(request,'register1.html',{'form':f})


def hospitalloginview(request):
    if request.method=='POST':
        # form= hospitalloginform(request.POST)
        # user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
        # if user:
        #     login(request,user)
        #     return redirect('hospital')
        # else:
        #     messages.info(request,'username or password is wrong')
        #     return redirect('')
        form=hospitalloginform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('myapp1:hospital')
    f=hospitalloginform()
    return render(request,'login2.html',{'form':f})


def hospital(request):
      return render(request,'hospital.html')



def bloodbank(request):
    return render(request,'blood.html')


# def appiontmentview(request):
#     return render(request,'patientinfo.html')
