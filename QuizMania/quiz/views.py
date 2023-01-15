from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Quiz
from .forms import QuizForm, QuestionForm, ChoiceForm
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
        if request.method == 'POST':

            question_form = QuestionForm(request.POST)
            choice_form = [ChoiceForm(request.POST,prefix=i) for i in range(4)]

            if question_form.is_valid() and choice_form.is_valid():

                ques.quiz = Quiz.objects.get(pk = id)
                ques = question_form.save()
                for i in range(4):
                    choice_form[i].question = ques
                    choice_form[i].save()
                    redirect("add_question/{id}/")
            else:
                form = question_form
                form_choice = [ChoiceForm()]*4

        else:
            form = QuestionForm()
            form_choice = [ChoiceForm()]*4
        return render(request,'quiz/add_questions.html',{'form':form,'form_choice':form_choice})


                
