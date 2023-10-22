from django.urls import reverse_lazy
from django.views.generic import CreateView, View, TemplateView
from django.contrib.auth import login, get_user_model
from django.core.mail import send_mail
from django.shortcuts import redirect
from django_conf import settings
from authapp.forms import StudentUserRegisterForm
from authapp.mixins import StudentUserIsNotAuthenticated
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.utils.safestring import mark_safe

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


class CustomLoginView(LoginView):
    def form_valid(self, form):
        ret = super().form_valid(form)
        # message = _("Login success!<br>Hi, %(username)s") % {
        #     "username": self.request.user.get_full_name()
        #     if self.request.user.get_full_name()
        #     else self.request.user.get_username()
        # }
        message = 'Login success!'
        messages.add_message(self.request, messages.INFO, mark_safe(message))
        return ret

    def form_invalid(self, form):
        for _unused, msg in form.error_messages.items():
            messages.add_message(self.request,
                                 messages.WARNING,
                                 mark_safe(f"Something goes wrong:<br>{msg}"), )
        return self.render_to_response(self.get_context_data(form=form))


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.add_message(self.request, messages.INFO, ("See you later!"))
        return super().dispatch(request, *args, **kwargs)