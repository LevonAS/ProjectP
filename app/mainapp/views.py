from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import mainapp.models as mainapp_models
from django.db.models import Q

from django_conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from mainapp.models import Subscriber, Tag



def index(request):
    context = {}
    #  Курсы за исключением первого, первые три
    context['courses'] = mainapp_models.Course.objects.exclude(slug='first-course')[:3]
    # Первый курс выбирается по слагу first-course
    context['first_course'] = get_object_or_404(mainapp_models.Course, slug='first-course')
    # return HttpResponse("Главная")
    # print(' /// context_main : ', context)
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
    course = get_object_or_404(mainapp_models.Course, slug=slug)
    # print(' /// context_course : ', course, course.benefits.all())

    context = {}
    context['course'] = get_object_or_404(mainapp_models.Course, slug=slug)
    # print(' /// context_course : ', context)
    return render(request, 'mainapp/course.html', context)