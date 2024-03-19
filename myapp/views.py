from django.shortcuts import render 
from django.http import HttpResponse 
from django.urls import reverse 
from django.contrib import messages 
from .models import patientregistermodel 
from .forms import patientregisterform,patientloginform
from django.contrib.auth import authenticate,login 
 
# Create your views here. 
def home(request):
    return render(request,'home.html')
def hospital(request):
    return render(request,'hospital.html')

def blood(request):
    return render(request,'blood.html')

def register(request): 
    if request.method == 'POST': 
        form = patientregisterform(request.POST,request.FILES) 
        if form.is_valid(): 
            print(request.POST) 
            form.save() 
    f=patientregisterform() 
    return render(request,'register.html',context={'form':f}) 

def patientloginview(request):
    if request.method=='POST':
        form=patientloginform(request.POST,request.FILES)
        if form.is_valid():
            # user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            # if user:
            #     login(request,user)
            #     return redirect('hospital')
            # else:
            #     messages.info(request,'username or password is wrong')
            #     return redirect('hospital')
            # print(request.POST) 
            form.save() 
    a=patientloginform()
    return render(request,'loginview.html',context={'a':a})





