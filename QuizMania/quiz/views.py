from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.models import User
from .forms import QuizForm
# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    return render(request,'quiz/dashboard.html')

@login_required(login_url='login')
def createQuiz(request):
    user = request.user
    if user.role == "QUIZMAKER":
        if request.method == "POST":
            form = QuizForm(request.POST)
            if form.is_valid():
                form.save()
                # change this
                return redirect(f'add_questions/{form.instance.pk}/')
        else:
            form = QuizForm()
        return render(request,'quiz/create_quiz.html',{'form':form})

@login_required(login_url='login')
def addQuestions(request,id):
    user = request.user
    if user.role == "QUIZMAKER":
        if request.method == "POST":
            form = QuizForm(request.POST)
            if form.is_valid():
                form.save()
                # change this
                return redirect(f'add_questions/{form.instance.pk}/')
        else:
            form = QuizForm()
        return render(request,'quiz/create_quiz.html',{'form':form})


                
