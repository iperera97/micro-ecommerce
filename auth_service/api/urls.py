from django.urls import path

from .views import UserSignupView

app_name = "api"
urlpatterns = [
    path('sign-up/', UserSignupView.as_view(), name="sign-up"),
]