
# import form class from django
from django import forms
 
# import GeeksModel from models.py
from .models import Quiz, Question, Choice 
 
# create a ModelForm
class QuizForm(forms.ModelForm):
    model = Quiz
    fields = ['title']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ("question",)


class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice 
        fields = ("choice","is_correct")



