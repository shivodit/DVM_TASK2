from django.db import transaction
from .models import QuizMaker,QuizTaker,User
from django.contrib.auth.forms import UserCreationForm

class MakerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
    def save(self, commit=True):
        user = super(MakerSignUpForm, self).save(commit=False)
        user.role = "QUIZMAKER"
        if commit:
            user.save()
        return user

        

class TakerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
    def save(self, commit=True):
        user = super(TakerSignUpForm, self).save(commit=False)
        user.role = "QUIZTAKER"
        if commit:
            user.save()
        
        return user


        