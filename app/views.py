from os import access

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from app.serializers import RegisterSerializer


class RegisterAPI(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"massage": "register successfully !!!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPI(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)

        return Response({
            "message": "Successfully logged in",
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh)
        })

# Đăng xuất (JWT)
class LogoutAPI(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout OK!"})
        except Exception:
            return Response({"message": "Invalid token"}, status=400)

class UserProfileAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"user": request.user.username})
