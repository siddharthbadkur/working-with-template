
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request,'register.html')

# def register(request):
#     print(request.method)
#     print(request.POST)
#     name=request.POST.get('name')
#     email=request.POST.get('email')
#     contact=request.POST.get('contact')
#     StudentModel.objects.create(Name=name,Email=email,Contact=contact)
#     data=StudentModel.objects.all()
#     print(data)
#     return HttpResponse ('data save succesfully')
def register(request):
    name=request.POST.get('name')
    print(name)
    return  HttpResponse(request,'login.html')


    
