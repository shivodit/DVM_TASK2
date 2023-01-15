from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        QTAKER = "QUIZTAKER", 'Quiz Taker'
        QMAKER = "QUIZMAKER", 'Quiz Maker'
    
    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def __str__(self):
        return self.username
    

class QuizTakerManager(BaseUserManager):
    def get_queryset(self,*args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role = User.Role.QTAKER)

class QuizTaker(User):

    base_role  = User.Role.QTAKER
    quiztaker = QuizTakerManager()

    class Meta: 
        proxy = True

    def welcome(self):
        return "Only for Quiz Takers"

class QuizMakerManager(BaseUserManager):
    def get_queryset(self,*args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role = User.Role.QMAKER)

class QuizMaker(User):

    base_role  = User.Role.QMAKER
    quizmaker = QuizMakerManager()

    class Meta: 
        proxy = True

    def welcome(self):
        return "Only for Quiz Takers"