from django.urls import path
from accounts.views import ForgotPasswordView, SignupView, LogoutView


urlpatterns = [
    # Endpoint posts from views.ForgotPasswordView
    path('api/forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    # Endpoint posts from views.SignupView
    path('api/signup/', SignupView.as_view(), name='signup'),
    # Endpoint posts from views.logout_view
    path('api/logout/', LogoutView.as_view(), name='logout'),
]