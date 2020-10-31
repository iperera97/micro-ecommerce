from django.conf import settings

from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import jwt

from .serializers import SignupSerializer, UserSerializer


class UserSignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer


class UserJWTView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_data = UserSerializer(instance=request.user).data
        token = jwt.encode(user_data, settings.SECRET_KEY, algorithm='HS256')
        return Response(headers={"jwt": token})