from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from authapp.models import StudentUser


def index(request):
    context = {}
    # return HttpResponse("Главная")
    return render(request, 'mainapp/index.html', context)




def view_login(request):
    context = {}

    # получаем из данных запроса POST отправленные через форму данные
    email = request.POST.get("email", "Undefined")
    password = request.POST.get("password", 1)
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        # return render(request, 'mainapp/index.html', context)
        return redirect(index)
    else:
        return HttpResponse(f"<h2>Email: {email}  Password: {password}</h2>")

def view_logout(request):
    context = {}

    logout(request)
    return redirect(index)
    # return render(request, 'mainapp/index.html', context)

def view_registration(request):
    first_name = request.POST.get("name", "Undefined")
    email = request.POST.get("email", "Undefined")
    phone_number = request.POST.get("phone", 1)
    password = request.POST.get("password", 1)

    try:
        user_email = StudentUser.objects.get(email=email)
    except (TypeError, ValueError, OverflowError, StudentUser.DoesNotExist):
        user_email = None
    else:
        return render(request, 'mainapp/thing/errors.html', {'err_text': f'Пользователь с таким e-mail: {email} уже существует'})

    try:
        user_phone = StudentUser.objects.get(phone_number=phone_number)
    except (TypeError, ValueError, OverflowError, StudentUser.DoesNotExist):
        user_phone = None
    else:
        return render(request, 'mainapp/thing/errors.html', {'err_text': f'Пользователь с таким номером телефона: {phone_number} уже существует'})

    user = StudentUser.objects.create_user(first_name, email, phone_number, password)
    # user.last_name = "Lennon"
    user.save()

    user = authenticate(request, email=email, password=password)
    login(request, user)

    return redirect(index)
