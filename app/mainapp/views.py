from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import mainapp.models as mainapp_models


def index(request):
    context = {}
    context['courses'] = mainapp_models.Course.objects.exclude(slug='first-course')[:3]
    context['first_course'] = get_object_or_404(mainapp_models.Course, slug='first-course')
    # return HttpResponse("Главная")
    return render(request, 'mainapp/index.html', context)
