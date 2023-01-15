from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('login/',LoginView.as_view(),name="login"),
    path('register/',views.registerView,name="register"),
    path('register_quiz_taker/',views.takerRegisterView,name="qt_register"),
    path('register_quiz_maker/',views.makerRegisterView,name="qm_register"),
    path('logout/',LogoutView.as_view(),name="logout"),
]