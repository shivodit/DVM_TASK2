from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('',views.dashboard,name='dashboard'),
    path('create_new_quiz/',views.createQuiz,name="create_quiz"),
    path('add_questions/<id>/',views.addQuestions,name="add_question"),
    path('delete_questions/<id>/',views.deleteQuestions,name="delete_question"),
    path('showQuiz/<id>/',views.showQuiz,name="show_quiz"),
]