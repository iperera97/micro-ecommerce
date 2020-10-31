from django.urls import path

from oauth2_provider.views import TokenView

from .views import UserSignupView, UserJWTView

app_name = "api"
urlpatterns = [
    path('sign-up/', UserSignupView.as_view(), name="sign-up"),
    path('sign-in/', TokenView.as_view(), name="sign-in"),
    path('user-jwt/', UserJWTView.as_view(), name="user-jwt"),
]
