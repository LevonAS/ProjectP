from django.urls import reverse_lazy
from django.views.generic import CreateView, View, TemplateView
from django.contrib.auth import login, get_user_model
from django.core.mail import send_mail
from django.shortcuts import redirect

from django_conf import settings

from authapp.forms import StudentUserRegisterForm
from authapp.mixins import StudentUserIsNotAuthenticated


User = get_user_model()


class StudentRegisterView(StudentUserIsNotAuthenticated, CreateView):
    form_class = StudentUserRegisterForm
    success_url = reverse_lazy('index')
    template_name = 'authapp/registration.html'
    # success_message = 'Вы зарегистрированы!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация на сайте'
        return context

    def form_valid(self, form):
        user = form.save()
        activation_link = reverse_lazy('authapp:confirm_email', kwargs={'email': user.email,
                                                                        'activation_key': user.activation_key})

        send_mail(
            'Подтвердите свой адрес электронной почты',
            f'Для подтверждения адреса электронной почты перейдите, пожалуйста, по ссылке:'
            f'{settings.DOMAIN_NAME}{activation_link}',
            'pereverzeva.mary@gmail.com',
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
