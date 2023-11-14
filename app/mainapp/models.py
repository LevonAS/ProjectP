import os
from django.conf import settings
from django.core.validators import EmailValidator
from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from uuid import uuid4


class Benefit(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    title = models.CharField(verbose_name="Польза", max_length=150)
    image = models.ImageField(verbose_name="Изображение", blank=True, null=True, upload_to="benefit_img/")
    deleted = models.BooleanField(verbose_name="Удален", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Польза"
        verbose_name_plural = "Польза"
        ordering = ["title"]


class Talent(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    title = models.CharField(verbose_name="Талант", max_length=255)
    description = models.TextField(verbose_name="Описание", blank=True)
    image = models.ImageField(verbose_name="Изображение", blank=True, null=True, upload_to="talent_img/")
    deleted = models.BooleanField(verbose_name="Удален", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Талант"
        verbose_name_plural = "Таланты"
        ordering = ["title"]


class Mentor(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    first_name = models.CharField(verbose_name="Имя ментора", max_length=150)
    last_name = models.CharField(verbose_name="Фамилия ментора", max_length=150)
    photo = models.ImageField(verbose_name="Фото ментора", blank=True, null=True, upload_to="mentor")
    status = models.CharField(verbose_name="Статус", max_length=255)
    quote = models.TextField(verbose_name="Высказывание")
    experience = models.TextField(verbose_name="Образование и Опыт")
    credo = models.TextField(verbose_name="Кредо и Сильные стороны")
    approach = models.TextField(verbose_name="Подход в обучении")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Ментор"
        verbose_name_plural = "Менторы"
        ordering = ["last_name", "first_name"]


class Preparation(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    value = models.CharField(verbose_name="Значение", max_length=50)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Уровень подготовки"
        verbose_name_plural = "Уровни подготовки"


class Course(models.Model):
    class CourseCategory(models.TextChoices):
        ART = ("ART", "ИСКУССТВО")
        DESIGN = ("DESIGN", "ДИЗАЙН")
        SOFT_SKILLS = ("SOFT_SKILLS", "SOFT SKILLS")

    id = models.UUIDField(default=uuid4, primary_key=True)
    title = models.CharField(verbose_name="Название курса", max_length=150)
    slug = models.SlugField(verbose_name="URL", max_length=200, unique=True, blank=True, null=True)
    category = models.CharField(verbose_name="Категория курса", max_length=11, choices=CourseCategory.choices)
    note = models.CharField(verbose_name="Цель курса", max_length=200, blank=True)
    description = models.TextField(verbose_name="Описание курса", blank=True)
    price = models.IntegerField(verbose_name="Стоимость курса")
    image = models.ImageField(verbose_name="Изображение", blank=True, null=True, upload_to="сourses_images")
    talents = models.ManyToManyField(Talent, verbose_name="Навыки, которые дает курс", related_name="courses")
    benefits = models.ManyToManyField(Benefit, verbose_name="Польза курса", related_name="courses")
    duration = models.CharField(verbose_name="Продолжительность курса", max_length=25, blank=True)
    age_group = models.CharField(verbose_name="Возрастная группа", max_length=25, blank=True)
    tools = models.TextField(verbose_name="Необходимые материалы и инструменты для курса", blank=True)
    preparation = models.ForeignKey(Preparation, verbose_name="Уровень подготовки", on_delete=models.CASCADE,
                                    null=True, related_name="courses")
    filling = models.TextField(verbose_name="Наполнение курса", blank=True)
    mentors = models.ManyToManyField(Mentor, verbose_name="Менторы", related_name="courses")
    question_lessons_features = models.TextField(verbose_name="Как проходят занятия на курсе?")
    question_access_duration = models.TextField(verbose_name="На сколько по времени доступен курс?")
    question_homework = models.TextField(verbose_name="Что насчет домашнего задания?")
    question_joining_telegram_chat = models.TextField(verbose_name="Что я получу, вступив в телеграм-канал курса?")
    question_paid_no_access = models.TextField(verbose_name="Я оплатил и не получил доступ к курсу")
    telegram_channel_link = models.URLField(verbose_name="Ссылка на тг-канал", blank=True, null=True)
    is_popular = models.BooleanField(verbose_name="Популярный", default=False)
    created_at = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    deleted = models.BooleanField(verbose_name="Удален", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["title"]

    def get_final_price(self, discount):
        final_price = self.price - self.price * discount / 100
        return final_price

    def get_quantity_lessons(self,):
        qty = len(self.lessons.all())
        if qty in [11, 12, 13, 14]:
            return f'{qty} уроков'
        if qty % 10 == 1:
            return f'{qty} урок'
        if qty % 10 in [2, 3, 4]:
            return f'{qty} урока'
        else:
            return f'{qty} уроков'


class Lesson(models.Model):
    class LessonType(models.TextChoices):
        ONLINE_LESSON = ("Online lesson", "Онлайн-урок")
        VIDEO_LESSON = ("Video lesson", "Видеоурок")

    id = models.UUIDField(default=uuid4, primary_key=True)
    title = models.CharField(verbose_name="Название урока", max_length=150)
    number = models.IntegerField(verbose_name="Номер урока")
    course = models.ForeignKey(Course, verbose_name="Курс", on_delete=models.CASCADE, related_name="lessons")
    type = models.CharField(verbose_name="Тип урока", max_length=13, choices=LessonType.choices)
    lesson_goal = models.TextField(verbose_name="Цель урока", blank=True)
    new_skill = models.TextField(verbose_name="Чему научится ребенок", blank=True)
    materials = models.TextField(verbose_name="Что нужно для урока", blank=True)
    image = models.ImageField(verbose_name="Изображение", blank=True, null=True, upload_to="lessons_img/")
    description = models.TextField(verbose_name="Описание урока", blank=True)
    video_file = models.FileField(verbose_name="Видео в записи", blank=True, null=True,
                                  upload_to="lessons_videos/")
    pdf_file = models.FileField(verbose_name="Дополнительный файл", blank=True, null=True,
                                upload_to="lessons_files/")
    link = models.CharField(verbose_name="Ссылка на онлайн-урок", max_length=150, blank=True)
    lesson_date = models.DateTimeField(verbose_name="Дата онлайн-урока", blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    deleted = models.BooleanField(verbose_name="Удален", default=False)

    def __str__(self):
        return f'Курс "{self.course}", Урок {self.number}: {self.title} '

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ["course", "number"]


class StudentsWork(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    title = models.CharField(verbose_name="Название", max_length=250)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Студент",
                             on_delete=models.SET_NULL, null=True, related_name="studentworks")
    image = models.ImageField(verbose_name="Изображение", blank=True, null=True, upload_to="students_best_pics_files/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Работа студента"
        verbose_name_plural = "Работы студентов"


class StudentsHomework(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    lesson = models.ForeignKey(Lesson, verbose_name="Урок", on_delete=models.CASCADE, null=True,
                               related_name="studenthomework")
    student = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Студент", on_delete=models.CASCADE,
                                related_name="studenthomework")
    image1 = models.ImageField(verbose_name="Изображение", blank=True, null=True, upload_to="homework_files/")
    image2 = models.ImageField(verbose_name="Изображение", blank=True, null=True, upload_to="homework_files/")
    image3 = models.ImageField(verbose_name="Изображение", blank=True, null=True, upload_to="homework_files/")
    pdf_file = models.FileField(verbose_name="Дополнительный файл", blank=True, null=True,
                                upload_to="homework_files/")
    comment_student = models.TextField(verbose_name="Комментарий студента", blank=True)
    comment_mentor = models.TextField(verbose_name="Комментарий ментора", blank=True)

    def __str__(self):
        return f'Домашнее задание к уроку {self.lesson}'

    class Meta:
        verbose_name = "Домашнее задание студента"
        verbose_name_plural = "Домашние задания студентов"


class Subscriber(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    first_name = models.CharField(verbose_name="Имя", max_length=30)
    email = models.EmailField(verbose_name="Адрес электронной почты", unique=True, validators=[EmailValidator])

    def __str__(self):
        return f'{self.first_name} {self.email}'

    class Meta:
        verbose_name = "Подписчик на новостную рассылку"
        verbose_name_plural = "Подписчики на новостную рассылку"
        ordering = ["first_name", "email"]

    @staticmethod
    def get_subscriber(email):
        return Subscriber.objects.filter(email=email).first()


class PromoCode(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    text = models.CharField(verbose_name="Промокод", max_length=50, unique=True)
    discount = models.IntegerField(verbose_name="Скидка в %")
    for_students = models.BooleanField(verbose_name="Для зарегистрированных пользователей")
    for_subscribers = models.BooleanField(verbose_name="Для подписчиков на новости")
    for_user = models.EmailField(verbose_name="Промокод для конкретного юзера (указать email)", blank=True, null=True)
    created_at = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    expiration_date = models.DateTimeField(verbose_name="Действует до")
    deleted = models.BooleanField(verbose_name="Удален", default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Промокод"
        verbose_name_plural = "Промокоды"
        ordering = ["-created_at"]

    def is_promocode_expired(self):
        if now() <= self.expiration_date:
            return False
        else:
            return True

    def is_promocode_for_user(self, email):
        return self.objects.filter(for_user=email).first()


class StudentCourse(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Студент",
                             on_delete=models.CASCADE, null=False, related_name="student")
    course = models.ForeignKey(Course, verbose_name="Курс", on_delete=models.CASCADE, related_name="course", null=False)
    lesson_number = models.IntegerField(verbose_name="Номер доступного урока", default=1)
    note = models.TextField(verbose_name="Примечания по студенту на этом курсе", blank=True)
    purchase_price = models.IntegerField(verbose_name="Цена покупки", blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    deleted = models.BooleanField(verbose_name="Удален", default=False)

    def __str__(self):
        return f'{self.user.first_name} {self.course.title}'

    class Meta:
        verbose_name = "Курс студента"
        verbose_name_plural = "Курс студента"
        ordering = ["-created_at"]
