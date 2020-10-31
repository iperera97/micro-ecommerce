from rest_framework import generics

from .serializers import SignupSerializer


class UserSignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer
