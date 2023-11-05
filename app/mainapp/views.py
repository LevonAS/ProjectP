from django_conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

import mainapp.models as mainapp_models
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
    ''' Страница вывода конкретного курса '''
    current_number = 1
    current_user = request.user


    course = get_object_or_404(mainapp_models.Course, slug=slug)
    descriptions = course.description.split('\n')

    if current_user.is_authenticated:
        # Необходимо установить current_number для текущего пользователя на этот курс (default 1)
        studentCourse = mainapp_models.StudentCourse.objects.filter(user=current_user) & mainapp_models.StudentCourse.objects.filter(course=course)
        if studentCourse:
            current_number = studentCourse[0].lesson_number

    lessons = mainapp_models.Lesson.objects.filter(course=course)
    for lesson in lessons:
        lesson.material = lesson.materials.split('\n')
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

        # Проверяем есть ли запись у пользователя о наличии первого курса. Если нет, то добавляем ее ему
        user_first_course = current_user.courses.filter(slug='first-course')
        if user_first_course:
            pass
        else:
             # В таблице StudentCourse необходимо сделать соответствующую запись
            studentCourse = mainapp_models.StudentCourse()
            studentCourse.user = current_user
            studentCourse.course = first_course
            studentCourse.lesson_number = 1
            studentCourse.save()

            first_course.students.add(current_user)
            first_course.save()

        context = {'courses': courses,
                   'first_course': first_course,
                   'descriptions_first': descriptions_first,
                   'user': current_user,
                   }
        return render(request, 'mainapp/user_page.html', context)
    else:
        messages.error(request, 'Для входа в личный кабинет Вам необходимо авторизоваться')
        return redirect('index')


def user_buy_course(request, slug):
    current_user = request.user
    course = get_object_or_404(mainapp_models.Course, slug=slug)
    if current_user.is_authenticated:
        if current_user not in course.students.all():
            # В таблице StudentCourse необходимо сделать соответствующую запись
            studentCourse = mainapp_models.StudentCourse()
            studentCourse.user = current_user
            studentCourse.course = course
            studentCourse.lesson_number = 1
            studentCourse.save()

            course.students.add(current_user)
            course.save()
            messages.info(request, f'Поздравляем! Вы записаны на курс {course.title}')


            return redirect('self-account')
        else:
            messages.info(request, f'Вы уже записаны на курс {course.title}')
            return redirect('self-account')
    else:
        messages.error(request, 'Для того чтобы записаться на курс Вам необходимо авторизоваться')
        return redirect('index')
