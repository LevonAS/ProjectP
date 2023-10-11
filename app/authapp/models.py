from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db import models
from django.utils.timezone import now
from datetime import timedelta
from uuid import uuid4


class StudentUser(AbstractUser):
    id = models.UUIDField(default=uuid4, primary_key=True)
    username = None
    first_name = models.CharField(verbose_name="Имя", max_length=150, blank=False)
    email = models.EmailField(verbose_name="Адрес электронной почты", unique=True, blank=False,
                              validators=[EmailValidator])
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=11, unique=True, blank=False)
    password_hash = models.CharField(max_length=65, blank=False)
    age = models.IntegerField(verbose_name="Возраст")
    created_at = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    deleted = models.BooleanField(default=False)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [first_name]

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True
