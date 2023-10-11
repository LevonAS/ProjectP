from django.conf import settings
from django.db import models
from uuid import uuid4


class Advantage(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    title = models.CharField(verbose_name="Преимущество", max_length=150)
    description = models.TextField(verbose_name="Описание", blank=True)
    image = models.ImageField(verbose_name="Изображение", blank=True, null=True, upload_to="")
    deleted = models.BooleanField(verbose_name="Удален", default=False)

    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"
        ordering = ["title"]


class QuestionAnswer(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    question = models.TextField(verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")
    deleted = models.BooleanField(verbose_name="Удален", default=False)

    class Meta:
        verbose_name = "Вопрос - ответ"
        verbose_name_plural = "Вопросы - ответы"


class Tag(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    text = models.CharField(verbose_name="Текст", max_length=50)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ["text"]


class Benefit(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    title = models.CharField(verbose_name="Польза", max_length=150)
    image = models.ImageField(verbose_name="Изображение", blank=True, null=True, upload_to="")
    deleted = models.BooleanField(verbose_name="Удален", default=False)

    class Meta:
        verbose_name = "Польза"
        verbose_name_plural = "Польза"
        ordering = ["title"]


class Talent(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    title = models.CharField(verbose_name="Талант", max_length=255)
    description = models.TextField(verbose_name="Описание", blank=True)
    image = models.ImageField(verbose_name="Изображение", blank=True, null=True, upload_to="")
    deleted = models.BooleanField(verbose_name="Удален", default=False)

    class Meta:
        verbose_name = "Талант"
        verbose_name_plural = "Таланты"
        ordering = ["title"]


class Course(models.Model):
    class CourseCategory(models.TextChoices):
        ART = ("ART", "искусство")
        DESIGN = ("DESIGN", "дизайн")
        SOFT_SKILLS = ("SOFT_SKILLS", "soft skills")

    id = models.UUIDField(default=uuid4, primary_key=True)
    title = models.CharField(verbose_name="Название курса", max_length=150)
    description = models.TextField(verbose_name="Описание курса", blank=True)
    price = models.FloatField(verbose_name="Стоимость курса")
    image = models.ImageField(verbose_name="Изображение", blank=True, null=True, upload_to="")
    teaser_video = models.FilePathField(verbose_name="Тизер-видео", blank=True, null=True, path="")
    category = models.CharField(verbose_name="Категория курса", max_length=11, choices=CourseCategory.choices)
    created_at = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    deleted = models.BooleanField(verbose_name="Удален", default=False)
    tags = models.ManyToManyField(Tag, verbose_name="Теги курса")
    benefits = models.ManyToManyField(Benefit, verbose_name="Польза курса")
    talents = models.ManyToManyField(Talent, verbose_name="Навыки, которые дает курс")
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="Студенты курса")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["title"]


class Mentor(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    first_name = models.CharField(verbose_name="Имя ментора", max_length=150)
    last_name = models.CharField(verbose_name="Фамилия ментора", max_length=150)
    photo = models.ImageField(verbose_name="Фото ментора", blank=True, null=True, upload_to="")
    courses = models.ManyToManyField(Course, verbose_name="")

    class Meta:
        verbose_name = "Ментор"
        verbose_name_plural = "Менторы"
        ordering = ["last_name", "first_name"]


class Application(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    approved = models.BooleanField(verbose_name="Заявка подтверждена", default=False)
    created_at = models.DateTimeField(verbose_name='Создан', auto_now_add=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ["created_at"]


class Videolesson(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    title = models.CharField(verbose_name="Название видеоурока", max_length=150)
    description = models.TextField(verbose_name="Описание видеоурока", blank=True)
    path_to_file = models.FilePathField(path="")
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Изображение", blank=True, null=True, upload_to="")
    created_at = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    viewed = models.BooleanField(verbose_name="Просмотрен", default=False)
    deleted = models.BooleanField(verbose_name="Удален", default=False)

    class Meta:
        verbose_name = "Видеоурок"
        verbose_name_plural = "Видеоуроки"
        ordering = ["-created_at"]


class Onlinelesson(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    title = models.CharField(verbose_name="Название онлайн-урока", max_length=150)
    link = models.CharField(verbose_name="Ссылка на онлайн-урок", max_length=150)
    lesson_date = models.DateTimeField(verbose_name="Дата онлайн-урока")
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    deleted = models.BooleanField(verbose_name="Удален", default=False)
    students = models.ManyToManyField(settings.AUTH_USER_MODEL)

    class Meta:
        verbose_name = "Онлайн урок"
        verbose_name_plural = "Онлайн уроки"
        ordering = ["-created_at"]


class StudentsWork(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    title = models.CharField(verbose_name="Название", max_length=255)
    description = models.TextField(verbose_name="Описание", blank=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(verbose_name="Изображение", blank=True, null=True, upload_to="")

    class Meta:
        verbose_name = "Работа студента"
        verbose_name_plural = "Работы студентов"
