from django.urls import path
from accounts.views import ForgotPasswordView, SignupView, logout_view, LoginView


urlpatterns = [
    # Endpoint posts from views.ForgotPasswordView
    path('forgot-password', ForgotPasswordView.as_view(), name='forgot_password'),
    # Endpoint posts from views.SignupView
    path('signup', SignupView.as_view(), name='signup'),
    # Endpoint posts from views.LoginView
    path('login', LoginView.as_view(), name='login'),
    # Endpoint posts from views.logout_view
    path('logout', logout_view, name='logout'),
]