from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    context = {}
    # return HttpResponse("Главная")
    return render(request, 'mainapp/index.html', context)
