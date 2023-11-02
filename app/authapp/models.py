from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db import models
from django.utils.timezone import now
from datetime import timedelta
from uuid import uuid4

from mainapp.models import Course


class StudentUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, first_name, email, phone_number, password=None):
        """
        Creates and saves a User with the given first_name, email, phone_number and password.
        """
        if not email:
            raise ValueError('Необходимо задать адрес электронной почты')

        user = self.model(
            first_name=first_name,
            email=self.normalize_email(email),
            phone_number=phone_number
        )
        user.set_password(password)
        user.is_active = False
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, email, phone_number, password=None):
        """
        Creates and saves a SuperUser with the given first_name, email, phone_number and password.
        """
        user = self.create_user(
            first_name=first_name,
            email=email,
            phone_number=phone_number,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class StudentUser(AbstractUser):
    id = models.UUIDField(default=uuid4, primary_key=True)
    username = None
    first_name = models.CharField(verbose_name="Имя", max_length=30, blank=False)
    email = models.EmailField(verbose_name="Адрес электронной почты", unique=True, blank=False,
                              validators=[EmailValidator])
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=13, unique=True, blank=False)
    age = models.IntegerField(verbose_name="Возраст", blank=True, null=True)
    courses = models.ManyToManyField(Course, verbose_name="Курсы", blank=True, related_name="students")
    created_at = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    deleted = models.BooleanField(default=False)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

    objects = StudentUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'phone_number']

    def __str__(self):
        return f'{self.first_name} {self.email}'

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True
