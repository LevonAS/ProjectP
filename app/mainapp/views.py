from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import mainapp.models as mainapp_models
from django.db.models import Q

from django_conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from mainapp.models import Subscriber, Tag
from authapp import views as authapp_views



def index(request):
    context = {}
    #  Курсы за исключением первого, первые три
    courses = mainapp_models.Course.objects.exclude(slug='first-course')[:3]
    for course in courses:
        course.description = course.description.split('\n')
    # courses.description.str.split('\n')
    # descriptions = courses.description.split('\n')
    # Первый курс выбирается по слагу first-course
    first_course = get_object_or_404(mainapp_models.Course, slug='first-course')
    descriptions_first = first_course.description.split('\n')

    context = {'courses': courses,
               # 'descriptions': descriptions,
               'first_course': first_course,
               'descriptions_first': descriptions_first,
               }
    return render(request, 'mainapp/index.html', context)


def subscribe_view(request):
    first_name = request.POST.get("name")
    email = request.POST.get("email")

    if not all(
        [
            first_name,
            email,
        ]
    ):
        messages.error(request, message='Форма подписки на новости заполнена некорректно')
        return redirect('index')

    subscriber = Subscriber.objects.filter(email=email).first()
    if not subscriber:
        subscriber = Subscriber.objects.create(first_name=first_name, email=email)
        print(subscriber)
        return send_mail_to_subscribe_user(subscriber, request)
    elif subscriber.email == email:
        messages.error(request, message='Вы уже подписаны на новости')

    return redirect('index')


def send_mail_to_subscribe_user(user, request):
    send_mail(
        f'Подтверждение подписки на новости на сайте {settings.DOMAIN_NAME}',
        f'Поздравляем с подпиской на новости: {settings.DOMAIN_NAME}',
        f'{settings.EMAIL_HOST_USER}',
        [user.email],
        fail_silently=False,
    )

    messages.info(request, f'Первое письмо с сюрпризом уже на вашей почте - бежим проверять)))')
    return redirect('index')


def view_course(request, slug):
    current_number = 0
    current_user = request.user
    if current_user.is_authenticated:
        # Необходимо установить current_number для текущего пользователя на этот курс (default 1)
        current_number = 1

    ''' Страница вывода конкретного курса '''
    course = get_object_or_404(mainapp_models.Course, slug=slug)
    descriptions = course.description.split('\n')

    lessons = mainapp_models.Lessons.objects.filter(сourses=course)
    for lesson in lessons:
        lesson.description_part3 = lesson.description_part3.split('\n')
    # print('image: ', image)
    # for i in range(1,6):
    #     print(i)
    # print(' /// context_course : ', descriptions, ' |o|||o| ', course.filling.split('\n'))
    mentor = get_mentor_course(request, slug)

    context = {'course': course,
               'descriptions': descriptions,
               'course_tools': course.tools.split('\n'),
               'course_filling': course.filling.split('\n'),
               'lessons': lessons,
               'mentor': mentor,
               'current_number': current_number,
               }
    # print(' /// context_course : ', context)
    return render(request, 'mainapp/course.html', context)


def view_courses_all(request):
    #  Курсы за исключением первого, все
    courses = mainapp_models.Course.objects.exclude(slug='first-course')
    for course in courses:
        course.description = course.description.split('\n')

    # Первый курс выбирается по слагу first-course
    first_course = get_object_or_404(mainapp_models.Course, slug='first-course')
    descriptions_first = first_course.description.split('\n')

    context = {'courses': courses,
               'first_course': first_course,
               'descriptions_first': descriptions_first,
               }
    return render(request, 'mainapp/courses_all.html', context)


def get_mentor_course(request, slug):
    course = get_object_or_404(mainapp_models.Course, slug=slug)
    mentor = mainapp_models.Mentor.objects.filter(courses=course).first()

    return mentor


def view_self_account(request):

    current_user = request.user
    if current_user.is_authenticated:
        # courses = current_user.courses.all()
        courses = current_user.courses.exclude(slug='first-course')
        for course in courses:
            course.description = course.description.split('\n')
        first_course = get_object_or_404(mainapp_models.Course, slug='first-course')
        descriptions_first = first_course.description.split('\n')

        context = {'courses': courses,
                   'first_course': first_course,
                   'descriptions_first': descriptions_first,
                   'user': current_user,
                   }
        return render(request, 'mainapp/user_page.html', context)
    else:
        messages.error(request, 'Для входа в личный кабинет Вам необходимо авторизоваться')
        return redirect('index')