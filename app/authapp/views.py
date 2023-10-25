from django.urls import reverse_lazy
from django.views.generic import View, TemplateView
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django_conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.utils.safestring import mark_safe

from random import random
from hashlib import sha1

from authapp.models import StudentUser


User = get_user_model()


def login_view(request):
    context = {}

    # получаем из данных запроса POST отправленные через форму данные
    email = request.POST.get("email", "Undefined")
    password = request.POST.get("password", 1)
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        # return render(request, 'mainapp/index.html', context)
        return redirect('index')
    else:
        return HttpResponse(f"<h2>Email: {email}  Password: {password}</h2>")


def logout_view(request):
    context = {}

    logout(request)
    return redirect('index')
    # return render(request, 'mainapp/index.html', context)


def register_view(request):
    first_name = request.POST.get("name", "Undefined")
    email = request.POST.get("email", "Undefined")
    phone_number = request.POST.get("phone", 1)
    password = request.POST.get("password", 1)

    try:
        user_email = StudentUser.objects.get(email=email)
    except (TypeError, ValueError, OverflowError, StudentUser.DoesNotExist):
        user_email = None
    else:
        return render(request, 'mainapp/thing/errors.html',
                      {'err_text': f'Пользователь с таким e-mail: {email} уже существует'})

    try:
        user_phone = StudentUser.objects.get(phone_number=phone_number)
    except (TypeError, ValueError, OverflowError, StudentUser.DoesNotExist):
        user_phone = None
    else:
        return render(request, 'mainapp/thing/errors.html',
                      {'err_text': f'Пользователь с таким номером телефона: {phone_number} уже существует'})

    user = StudentUser.objects.create_user(first_name, email, phone_number, password)

    activation_link = create_activation_link(user)
    return send_mail_to_activate_user(user, activation_link)


def create_activation_link(user):
    salt = sha1(str(random()).encode('utf-8')).hexdigest()[:6]
    user.activation_key = sha1((user.email + salt).encode('utf-8')).hexdigest()
    user.save()

    activation_link = reverse_lazy('authapp:confirm_email', kwargs={'email': user.email,
                                                                    'activation_key': user.activation_key})

    return activation_link


def send_mail_to_activate_user(user, activation_link):
    send_mail(
        f'Подтвердите свой адрес электронной почты на сайте {settings.DOMAIN_NAME}',
        f'Для подтверждения адреса электронной почты перейдите, пожалуйста, по ссылке: '
        f'{settings.DOMAIN_NAME}{activation_link}. Ссылка действительна до {user.activation_key_expires}',
        f'{settings.EMAIL_HOST_USER}',
        [user.email],
        fail_silently=False,
    )
    return redirect('authapp:email_confirmation_sent')


class UserConfirmEmailView(View):
    def get(self, request, email, activation_key):
        try:
            user = User.objects.get(email=email)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            login(request, user, backend='authapp.auth.EmailAuthBackend')
            return redirect('authapp:email_confirmed')
        else:
            return redirect('authapp:email_confirmation_failed')


class EmailConfirmationSentView(TemplateView):
    template_name = 'authapp/email_confirmation_sent.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Письмо для подтверждения адреса электронной почты отправлено'
        return context


class EmailConfirmedView(TemplateView):
    template_name = 'authapp/email_confirmed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Адрес электронной почты подтвержден'
        return context


class EmailConfirmationFailedView(TemplateView):
    template_name = 'authapp/email_confirmation_failed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Адрес электронной почты не подтвержден'
        return context
