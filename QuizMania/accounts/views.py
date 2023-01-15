from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import MakerSignUpForm,TakerSignUpForm

# Create your views here.

# def loginView(request):
#     logout(request)
#     username = password = ''
#     if request.POST:
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return redirect('dashboard')
    
#     return render(request,'accounts/login.html',locals())


def registerView(request):
    return render(request,'registration/register_choice.html')

def takerRegisterView(request):
    if request.method == "POST":
        form = TakerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = TakerSignUpForm()
    return render(request,'registration/register.html',{'form':form})
    

def makerRegisterView(request):
    if request.method == "POST":
        form = MakerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = MakerSignUpForm()
    return render(request,'registration/register.html',{'form':form})
   

# def logoutView(request):
#     logout(request)
#     redirect('dashboard')