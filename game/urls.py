#url 설정

from django.urls import path
from .views import signup, puzzle_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("puzzle/", puzzle_view, name="puzzle"),
]