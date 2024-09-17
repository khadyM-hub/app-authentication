from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken

class ForgotPasswordView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        if not email:
            return JsonResponse({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Implement password reset logic (e.g., send email with reset link)
        send_mail(
            'Password Reset Request',
            'Please follow the instructions to reset your password.',
            'from@example.com',
            [email],
            fail_silently=False,
        )
        
        return JsonResponse({"message": "Password reset email sent"}, status=status.HTTP_200_OK)

class SignupView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return JsonResponse({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if user already exists
        if User.objects.filter(email=email).exists():
            return JsonResponse({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create the user
        user = User.objects.create_user(username=email, email=email, password=password)
        
        return JsonResponse({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate the user
        user = authenticate(request, email=email, password=password)

        if user is None:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

        # Login the user
        login(request, user)

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return Response({
            "access": access_token,
            "refresh": refresh_token,
            "user": {
                "email": user.email,
                "username": user.username
            }
        }, status=status.HTTP_200_OK)


def logout_view(request):
    from rest_framework_simplejwt.tokens import RefreshToken
    try:
        refresh_token = request.data.get('refresh')
        token = RefreshToken(refresh_token)
        token.blacklist()
        return JsonResponse({"detail": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return JsonResponse({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)