from django.db.models import Q
from django_conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone

import mainapp.models as mainapp_models
import authapp.models as authapp_models
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

    subscriber = mainapp_models.Subscriber.objects.filter(email=email).first()
    if not subscriber:
        subscriber = mainapp_models.Subscriber.objects.create(first_name=first_name, email=email)
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
        # print(' /// context_course : ', lesson.material)
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
    # print(' /// context_course : ', lesson.material)
    return render(request, 'mainapp/course.html', context)


def view_courses_all(request):
    #  Курсы за исключением первого, все
    courses = mainapp_models.Course.objects.exclude(slug='first-course')
    for course in courses:
        course.description = course.description.split('\n')

    # Первый курс выбирается по слагу first-course
    # first_course = get_object_or_404(mainapp_models.Course, slug='first-course')
    # descriptions_first = first_course.description.split('\n')

    # Первый курс также необходимо приобретать!
    first_course = mainapp_models.Course.objects.filter(slug='first-course')
    descriptions_first = None
    if first_course:
        first_course = first_course[0]
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
        account_courses = {}
        active_courses = 0
        completed_courses = 0
        # Получим все активные курсы пользователя кроме 1-ого
        # courses = current_user.courses.exclude(slug='first-course')
        courses = current_user.courses.all()
        for course in courses:
            account_courses[course.id] = {}

            account_courses[course.id]['title'] = course.title
            account_courses[course.id]['slug'] = course.slug
            account_courses[course.id]['image'] = course.image
            account_courses[course.id]['lesons_count'] = course.lessons.count()
            studentCourse = mainapp_models.StudentCourse.objects.filter(user=current_user) & mainapp_models.StudentCourse.objects.filter(course=course)
            if studentCourse:
                account_courses[course.id]['lesons_view'] = studentCourse[0].lesson_number - 1
            else:
                account_courses[course.id]['lesons_view'] = 0
            if account_courses[course.id]['lesons_count'] > account_courses[course.id]['lesons_view']:
                account_courses[course.id]['is_active'] = True
                active_courses += 1
            else:
                account_courses[course.id]['is_active'] = False
                completed_courses += 1

        # Первый курс также необходимо приобретать
        # first_course = current_user.courses.filter(slug='first-course')[0]
        # account_first = {}
        # first_course_buy = False
        # if first_course:
        #     first_course_buy = True
        #     account_first['title'] = first_course.title
        #     account_first['slug'] = first_course.slug
        #     account_first['lesons_count'] = first_course.lessons.count()
        #     studentCourse = mainapp_models.StudentCourse.objects.filter(
        #         user=current_user) & mainapp_models.StudentCourse.objects.filter(course=first_course)
        #     if studentCourse:
        #         account_first['lesons_view'] = studentCourse[0].lesson_number - 1
        #     else:
        #         account_first['lesons_view'] = 0
        #     if account_first['lesons_count'] > account_first['lesons_view']:
        #         account_first['is_active'] = True
        #         active_courses += 1
        #     else:
        #         account_first['is_active'] = False
        #         completed_courses += 1

        context = {'user': current_user,
                   'active_courses': active_courses,
                   'completed_courses': completed_courses,
                   'account_courses': account_courses,
                   # 'account_first': account_first,
                   # 'first_course_buy': first_course_buy,
                   }
        return render(request, 'mainapp/user_page.html', context)
    else:
        messages.error(request, 'Для входа в личный кабинет Вам необходимо авторизоваться')
        return redirect('index')


def user_buy_course(request, slug):
    print(request)
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

            if request.POST.get("promocode"):
                apply_promo(course, request, current_user)

            messages.info(request, f'Поздравляем! Вы записаны на курс {course.title}')

            return redirect('self-account')
        else:
            messages.info(request, f'Вы уже записаны на курс {course.title}')
            return redirect('self-account')
    else:
        messages.error(request, 'Для того чтобы записаться на курс Вам необходимо авторизоваться')
        return redirect('course', slug=course.slug)


def apply_promo(course, request, current_user):
    promocode_text = request.POST.get("promocode")
    promocode = mainapp_models.PromoCode.objects.filter(text=promocode_text).first()
    message_error = 'Промокод недействителен'

    if promocode and promocode.is_promocode_expired():
        if promocode.for_students and authapp_models.StudentUser.objects.filter(email=current_user.email).first():
            return course.get_final_price(promocode.discount)
        if promocode.for_subscribers and mainapp_models.Subscriber.objects.filter(email=current_user.email).first():
            return course.get_final_price(promocode.discount)
        if mainapp_models.PromoCode.is_promocode_for_user:
            return course.get_final_price(promocode.discount)

        return messages.error(request, message=message_error)
    else:
        return messages.error(request, message='Вы ввели неверный промокод, либо срок действия промокода истек')


def view_self_account_course(request, slug):
    current_user = request.user
    if current_user.is_authenticated:
        course = current_user.courses.filter(slug=slug)
        if course:
            student_course = mainapp_models.StudentCourse.objects.filter(user=current_user) & mainapp_models.StudentCourse.objects.filter(course=course[0])
            lessons = course[0].lessons.all().order_by('number')

            context = {'user': current_user,
                       'studentCourse': student_course[0],
                       'lessons': lessons,
                       'course': course[0],
                       }

            return render(request, 'mainapp/user_course.html', context)

        else:
            messages.error(request, 'У Вас нет такого курса!')
            return redirect('index')

    messages.error(request, 'Для данных действий необходимо авторизоваться')
    return redirect('index')


def view_self_account_course_lesson(request, slug, number, hw):
    current_user = request.user
    if current_user.is_authenticated:
        course = current_user.courses.filter(slug=slug)

        if course:
            student_course = mainapp_models.StudentCourse.objects.filter(Q(user=current_user) & Q(course=course[0]))
            student_course = student_course[0]

            lesson = course[0].lessons.filter(number=number)[0]
            lesson_desc = lesson.description.split('\n')
            lesson_count = course[0].lessons.count()

            btn_l = ''
            btn_r = ''
            if number == 1:
                if hw == 0:
                    btn_l = f'/self-account/lesson_zero/{slug}/'
                    btn_r = f'/self-account/lesson/{slug}/{number}/1/'
                else:
                    btn_l = f'/self-account/lesson/{slug}/{number}/0/'
                    btn_r = f'/self-account/lesson/{slug}/{number + 1}/0/'
            if number > 1 and number < lesson_count:
                if hw == 0:
                    btn_l = f'/self-account/lesson/{slug}/{number - 1}/1/'
                    btn_r = f'/self-account/lesson/{slug}/{number}/1/'
                else:
                    btn_l = f'/self-account/lesson/{slug}/{number}/0/'
                    btn_r = f'/self-account/lesson/{slug}/{number + 1}/0/'
            if number == lesson_count:
                if hw == 0:
                    btn_l = f'/self-account/lesson/{slug}/{number - 1}/1/'
                    btn_r = f'/self-account/lesson/{slug}/{number}/1/'
                else:
                    btn_l = f'/self-account/lesson/{slug}/{number}/0/'

            context = {'user': current_user,
                       'studentCourse': student_course,
                       'lesson': lesson,
                       'course': course[0],
                       'hw': hw,
                       'lesson_desc': lesson_desc,
                       'btn_l': btn_l,
                       'btn_r': btn_r,
                       }

            if student_course.lesson_number == number:
                print('LESSON от:', student_course.lesson_number)
                student_course.lesson_number = number + 1
                student_course.save()
                print('LESSON до:', student_course.lesson_number)

            return render(request, 'mainapp/user_lesson.html', context)

        else:
            messages.error(request, 'У Вас нет такого курса!')
            return redirect('index')

    messages.error(request, 'Для данных действий необходимо авторизоваться')
    return redirect('index')


def view_self_account_course_lesson_zero(request, slug):
    current_user = request.user
    if current_user.is_authenticated:
        course = current_user.courses.filter(slug=slug)

        if course:
            student_course = mainapp_models.StudentCourse.objects.filter(Q(user=current_user) & Q(course=course[0]))
            student_course = student_course[0]

            course_desc = course[0].description.split('\n')

            context = {'user': current_user,
                       'studentCourse': student_course,
                       'course': course[0],
                       'course_desc': course_desc,
                       }

            return render(request, 'mainapp/user_lesson_zero.html', context)

        else:
            messages.error(request, 'У Вас нет такого курса!')
            return redirect('index')

    messages.error(request, 'Для данных действий необходимо авторизоваться')
    return redirect('index')