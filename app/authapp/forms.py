from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from random import random
from hashlib import sha1

from authapp.models import StudentUser


class StudentUserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        label='Имя студента',
        help_text='Введите имя студента',
    )
    password1 = forms.CharField(label='Надежный пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повтор надежного пароля', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'email', 'phone_number', 'password1', 'password2')

    def clean_email(self):
        current_email = self.cleaned_data.get('email')
        if current_email and StudentUser.objects.filter(email=current_email).exists():
            raise forms.ValidationError('Пользователь с таким email уже зарегистрирован')

        return current_email

    def clean_phone_number(self):
        current_phone_number = self.cleaned_data.get('phone_number')
        if current_phone_number and StudentUser.objects.filter(phone_number=current_phone_number).exists():
            raise forms.ValidationError('Пользователь с таким номером телефона уже зарегистрирован')

        return current_phone_number

    def clean_password2(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['password1'] != cleaned_data['password2']:
            raise forms.ValidationError('Пароли не совпадают')

        return cleaned_data['password2']

    def save(self):
        user = super(StudentUserRegisterForm, self).save()

        user.is_active = False
        salt = sha1(str(random()).encode('utf-8')).hexdigest()[:6]
        user.activation_key = sha1((user.email + salt).encode('utf-8')).hexdigest()
        user.save()

        return user
