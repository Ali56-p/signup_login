from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.

def Homepage(request):

    return render(request,'home.html')

def Singup_page(request):
    if request.method=='POST':
         
         username = request.POST.get('First Name')
         uname2 = request.POST.get('Last Name')
         email = request.POST.get('email')
         password = request.POST.get('password')
         
         my_user = User.objects.create_user(username,email,password)
         my_user.save()
        
         return redirect('Login')
    return render(request,'signup.html')

def Login(request):
        if request.method == 'POST':
             email = request.POST.get('email1')
             password1 = request.POST.get('pass1')
             print(email)
             print(password1)

 
             user = authenticate(request, username=email, password=password1)
             if user is not None:
                  
                  login(request,user)
                  return redirect('HomePage')
             else:
                  return HttpResponse("Password or username not match")
              
             
        return render(request,'login.html')

