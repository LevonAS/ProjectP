from django.urls import path

from authapp.views import StudentRegisterView, EmailConfirmationSentView, UserConfirmEmailView, EmailConfirmedView,\
    EmailConfirmationFailedView

app_name = 'authapp'

urlpatterns = [
    path('register/', StudentRegisterView.as_view(), name='register'),
    path('email-confirmation-sent/', StudentRegisterView.as_view(), name='email_confirmation_sent'),
    path('confirm-email/<str:email>/<str:activation_key>/', UserConfirmEmailView.as_view(), name='confirm_email'),
    path('email-confirmed/', EmailConfirmedView.as_view(), name='email_confirmed'),
    path('email-confirmation-failed/', EmailConfirmationFailedView.as_view(), name='email_confirmation_failed'),
]
