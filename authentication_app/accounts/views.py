from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail  # Adjust as per your email backend
from django.contrib.auth.models import User
from django.http import JsonResponse

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

def logout_view(request):
    from rest_framework_simplejwt.tokens import RefreshToken
    try:
        refresh_token = request.data.get('refresh')
        token = RefreshToken(refresh_token)
        token.blacklist()
        return JsonResponse({"detail": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return JsonResponse({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)