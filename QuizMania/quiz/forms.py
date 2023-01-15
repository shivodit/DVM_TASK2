
# import form class from django
from django import forms
 
# import GeeksModel from models.py
from .models import Quiz, Question
 
# create a ModelForm
class QuizForm(forms.ModelForm):
    model = Quiz
    fields = ['title']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        