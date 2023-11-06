"""
URL configuration for django_conf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from mainapp import views as main_views
from authapp import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index, name='index'),
    path('login/', auth_views.login_view, name='login'),
    path('logout/', auth_views.logout_view),
    path('register/', auth_views.register_view),

    path('subscribe/', main_views.subscribe_view),
    path('courses/<str:slug>/', main_views.view_course, name='course'),
    path('courses-all/', main_views.view_courses_all, name='courses_all'),
    path('buy-course/<str:slug>/', main_views.user_buy_course, name='buy_course'),

    path('self-account/', main_views.view_self_account, name='self-account'),
    path('self-account/course/<str:slug>/', main_views.view_self_account_course, name='self-account-course'),
    # path('self-account/lesson/', main_views.view_self_account_course_lesson, name='self-account-lesson'),
    path('self-account/lesson/<str:slug>/<int:number>/<int:hw>/', main_views.view_self_account_course_lesson, name='self-account-lesson'),
    # path('self-account/course/<str:slug>/homework/<int:number>', main_views.view_self_account_course_lesson_hw, name='self-account-course-lesson-hw'),
    # path('courses/', include('mainapp.urls', namespace='courses')),
    path('authapp/', include('authapp.urls', namespace='authapp')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
