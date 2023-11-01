import os
from django.conf import settings
from django.core.validators import EmailValidator
from django.db import models
from django.urls import reverse
from uuid import uuid4


class Advantage(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    title = models.CharField(verbose_name="Преимущество", max_length=150)
    description = models.TextField(verbose_name="Описание", blank=True)
    image = models.ImageField(verbose_name="Изображение", blank=True, null=True, upload_to="")
    deleted = models.BooleanField(verbose_name="Удален", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"
        ordering = ["title"]


class Tag(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    text = models.CharField(verbose_name="Текст тега", max_length=50)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ["text"]


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
    note = models.CharField(verbose_name="Цель курса", default='', max_length=200)
    description = models.TextField(verbose_name="Описание курса", blank=True)
    price = models.FloatField(verbose_name="Стоимость курса")
    category = models.CharField(verbose_name="Категория курса", max_length=11, choices=CourseCategory.choices)
    tools = models.TextField(verbose_name="Необходимые материалы и инструменты для курса", blank=True)
    filling = models.TextField(verbose_name="Наполнение курса", blank=True)
    image = models.ImageField(verbose_name="Изображение", blank=True, null=True, upload_to="сourses_images")
    teaser_video = models.FilePathField(verbose_name="Тизер-видео", blank=True, null=True, path=os.path.join(settings.MEDIA_ROOT, "teaser_video"))
    created_at = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    tags = models.ManyToManyField(Tag, verbose_name="Теги курса", related_name="courses")
    benefits = models.ManyToManyField(Benefit, verbose_name="Польза курса", related_name="courses")
    talents = models.ManyToManyField(Talent, verbose_name="Навыки, которые дает курс", related_name="courses")
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="Студенты курса", related_name="courses")
    is_popular = models.BooleanField(verbose_name="Популярный", default=False)
    deleted = models.BooleanField(verbose_name="Удален", default=False)
    age_group = models.CharField(verbose_name="Возрастная группа", max_length=25, blank=True)
    lesson_qty = models.CharField(verbose_name="Количество уроков", max_length=25, blank=True)
    duration = models.CharField(verbose_name="Продолжительность курса", max_length=25, blank=True)
    preparation = models.ForeignKey(Preparation, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["title"]

    # def get_absolute_url(self):
    #     return reverse('courses: course_detail', args=[self.slug])


class Lesson(models.Model):
    VALUE_PART1 = 'Цель урока'
    VALUE_PART2 = 'Чему научится ребенок?'
    VALUE_PART3 = 'Что нужно для урока?'

    class LessonType(models.TextChoices):
        ONLINE_LESSON = ("Online lesson", "Онлайн-урок")
        VIDEO_LESSON = ("Video lesson", "Видеоурок")

    id = models.UUIDField(default=uuid4, primary_key=True)
    title = models.CharField(verbose_name="Название урока", max_length=150)
    number = models.IntegerField(verbose_name="Номер урока")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    type = models.CharField(verbose_name="Тип урока", max_length=13, choices=LessonType.choices)
    part1 = models.CharField(verbose_name="Название первой части описания урока", default=VALUE_PART1, max_length=150, blank=True)
    description_part1 = models.TextField(verbose_name="Содержание первой части", blank=True)
    part2 = models.CharField(verbose_name="Название второй части описания урока", default=VALUE_PART2, max_length=150, blank=True)
    description_part2 = models.TextField(verbose_name="Содержание второй части", blank=True)
    part3 = models.CharField(verbose_name="Название третьей части описания урока", default=VALUE_PART3, max_length=150, blank=True)
    description_part3 = models.TextField(verbose_name="Содержание третьей части", blank=True)
    image = models.ImageField(verbose_name="Изображение", blank=True, null=True, upload_to="lessons_img/")
    path_to_file = models.FilePathField(path=os.path.join(settings.MEDIA_ROOT, "video_lessons"), blank=True)
    link = models.CharField(verbose_name="Ссылка на онлайн-урок", max_length=150, blank=True)
    lesson_date = models.DateTimeField(verbose_name="Дата онлайн-урока", blank=True, null=True)
    viewed = models.BooleanField(verbose_name="Просмотрен", default=False)
    created_at = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    deleted = models.BooleanField(verbose_name="Удален", default=False)

    def __str__(self):
        return f'Курс "{self.course}", Урок {self.number}, {self.title} '

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ["course", "number"]


class QuestionAnswer(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    question = models.TextField(verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")
    course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)
    deleted = models.BooleanField(verbose_name="Удален", default=False)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Вопрос - ответ"
        verbose_name_plural = "Вопросы - ответы"


class Mentor(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    first_name = models.CharField(verbose_name="Имя ментора", max_length=150)
    last_name = models.CharField(verbose_name="Фамилия ментора", max_length=150)
    photo = models.ImageField(verbose_name="Фото ментора", blank=True, null=True, upload_to="mentor")
    status = models.CharField(verbose_name="Статус", max_length=255)
    experience = models.TextField(verbose_name="Образование и Опыт")
    credo = models.TextField(verbose_name="Кредо и Сильные стороны")
    approach = models.TextField(verbose_name="Подход в обучении")
    courses = models.ManyToManyField(Course, verbose_name="Курсы", related_name="mentors")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Ментор"
        verbose_name_plural = "Менторы"
        ordering = ["last_name", "first_name"]


class Application(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="applications")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="applications")
    approved = models.BooleanField(verbose_name="Заявка подтверждена", default=False)
    created_at = models.DateTimeField(verbose_name='Создана', auto_now_add=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ["created_at"]


class StudentsWork(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    title = models.CharField(verbose_name="Название", max_length=250)
    description = models.TextField(verbose_name="Описание", blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="studentworks")
    image = models.ImageField(verbose_name="Изображение", blank=True, null=True, upload_to="")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Работа студента"
        verbose_name_plural = "Работы студентов"


class PromoCode(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    text = models.CharField(verbose_name="Промокод", max_length=50)
    created_at = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    expiration_date = models.DateTimeField(verbose_name="Действует до")
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="promocodes")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Промокод"
        verbose_name_plural = "Промокоды"
        ordering = ["-created_at"]


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

