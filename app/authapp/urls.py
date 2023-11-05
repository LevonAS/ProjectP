from django.urls import path

from authapp.views import UserConfirmEmailView, ChangePasswordView

app_name = 'authapp'

urlpatterns = [
    path('confirm-email/<str:email>/<str:activation_key>/', UserConfirmEmailView.as_view(), name='confirm_email'),
    # я бы перенесла это в отдельное приложение account
    path('change-password/', ChangePasswordView.as_view(), name='change_password')
]
