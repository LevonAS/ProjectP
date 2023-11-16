from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView

from random import random
from hashlib import sha1

from authapp.models import StudentUser
from authapp.forms import ChangePasswordForm
from django_conf import settings


User = get_user_model()


def login_view(request):
    context = {}

    # получаем из данных запроса POST отправленные через форму данные
    email = request.POST.get("email", "Undefined")
    password = request.POST.get("password", 1)
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        # return render(request, 'mainapp/index.html', context)
        return redirect('index')
    else:
        messages.error(request, 'Вы неверно указали почту или пароль')
        # return HttpResponse(f"<h2>Email: {email}  Password: {password}</h2>")
        return redirect('index')


def logout_view(request):
    context = {}

    logout(request)
    return redirect('index')
    # return render(request, 'mainapp/index.html', context)


def register_view(request):
    first_name = request.POST.get("name")
    email = request.POST.get("email")
    phone_number = request.POST.get("phone")
    password = request.POST.get("password")

    if not all(
        [
            first_name,
            email,
            phone_number,
            password
        ]
    ):
        messages.error(request, message='Форма регистрации заполнена некорректно')
        return redirect('index')

    student = StudentUser.objects.filter(Q(email=email) | Q(phone_number=phone_number)).first()
    if not student:
        user = StudentUser.objects.create_user(first_name, email, phone_number, password)
        activation_link = create_activation_link(user)
        return send_mail_to_activate_user(user, activation_link, request)
    elif student.email == email:
        messages.error(request, message=f'Пользователь с таким email: {email} уже существует')
    elif student.phone_number == phone_number:
        messages.error(request, message=f'Пользователь с таким номером телефона: {phone_number} уже существует')

    return redirect('index')


def create_activation_link(user):
    salt = sha1(str(random()).encode('utf-8')).hexdigest()[:6]
    user.activation_key = sha1((user.email + salt).encode('utf-8')).hexdigest()
    user.save()

    activation_link = reverse_lazy('authapp:confirm_email', kwargs={'email': user.email,
                                                                    'activation_key': user.activation_key})

    return activation_link


def send_mail_to_activate_user(user, activation_link, request):
    send_mail(
        f'Подтвердите свой адрес электронной почты на сайте {settings.DOMAIN_NAME}',
        f'Для подтверждения адреса электронной почты перейдите, пожалуйста, по ссылке: '
        f'{settings.DOMAIN_NAME}{activation_link}. Ссылка действительна до {user.activation_key_expires}',
        f'{settings.EMAIL_HOST_USER}',
        [user.email],
        fail_silently=False,
    )

    messages.info(request, f'На ваш адрес электронной почты было отправлено письмо с подтверждением.\n'
                              f'Пожалуйста, проверьте свою электронную почту и нажмите на ссылку подтверждения, чтобы завершить регистрацию.\n'
                              f'Если письмо не пришло, проверьте папку спам.')
    return redirect('index')


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
            messages.success(request, 'Ваш адрес электронной почты успешно подтвержден. Спасибо за регистрацию!')
            return redirect('index')
        else:
            messages.error(request, 'Ссылка для подтверждения по электронной почте недействительна или срок ее действия'
                                    'истек. Пожалуйста, зарегистрируйтесь снова. Либо попробуйте войти в личный кабинет.')
            return redirect('index')


class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy("self-account")
    template_name = "mainapp/parts_pages/password_change.html"


# def reset_password_view(request):
#     email = request.POST.get("email")
#     if not email:
#         messages.error(request, message="Необходимо ввести email")
#         return redirect('index')
#
#     student = StudentUser.objects.filter(email=email).first()
#     if not student:
#         messages.error(request, message="Пользователь с таким адресом электронной почты не зарегистрирован")
#         return redirect('index')
#
#     if student.is_active:
#         token = PasswordResetTokenGenerator.make_token(student)


def password_reset_done_view(request):
    messages.info(request, message='Мы отправили вам инструкцию по установке нового пароля на указанный адрес электронной почты (если в нашей базе данных есть такой адрес). Вы должны получить ее в ближайшее время. Если вы не получили письмо, пожалуйста, убедитесь, что вы ввели адрес с которым Вы зарегистрировались, и проверьте папку со спамом.')
    return redirect('index')


def password_reset_complete_view(request):
    messages.info(request, message='Ваш пароль был сохранен. Теперь вы можете войти.')
    return redirect('index')
