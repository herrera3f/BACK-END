from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def login(request):
    return render(request,'login.html',{
        'form':UserCreationForm
    })

def home(request):
    return render(request,'home.html')
    
