from django.urls import path
from .views_api import PasswordResetAPIView, UserRegistrationAPIView

urlpatterns = [
    path('api/password/reset/', PasswordResetAPIView.as_view(), name='api_password_reset'),
    path('api/register/', UserRegistrationAPIView.as_view(), name='api_register'),
]
