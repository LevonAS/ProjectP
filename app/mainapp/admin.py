from django.contrib import admin

from mainapp.models import Advantage, QuestionAnswer, Tag, Benefit, Talent, Course, Mentor, Application,\
Videolesson, Onlinelesson, StudentsWork, PromoCode, Preparation, Subscriber


admin.site.register(Advantage)
admin.site.register(QuestionAnswer)
admin.site.register(Tag)
admin.site.register(Benefit)
admin.site.register(Talent)
admin.site.register(Mentor)
admin.site.register(Application)
admin.site.register(StudentsWork)
admin.site.register(PromoCode)
admin.site.register(Preparation)
admin.site.register(Subscriber)



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Videolesson)
class VideolessonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Onlinelesson)
class OnlinelessonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
