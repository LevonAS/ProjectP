from django.urls import path

from authapp.views import EmailConfirmationSentView, UserConfirmEmailView, EmailConfirmedView,\
    EmailConfirmationFailedView

app_name = 'authapp'

urlpatterns = [
    path('email-confirmation-sent/', EmailConfirmationSentView.as_view(), name='email_confirmation_sent'),
    path('confirm-email/<str:email>/<str:activation_key>/', UserConfirmEmailView.as_view(), name='confirm_email'),
    path('email-confirmed/', EmailConfirmedView.as_view(), name='email_confirmed'),
    path('email-confirmation-failed/', EmailConfirmationFailedView.as_view(), name='email_confirmation_failed'),
]
