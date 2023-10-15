from django.contrib import admin

from mainapp.models import Advantage, QuestionAnswer, Tag, Benefit, Talent, Course, Mentor, Application,\
                   Videolesson, Onlinelesson, StudentsWork, PromoCode


admin.site.register(Advantage)
admin.site.register(QuestionAnswer)
admin.site.register(Tag)
admin.site.register(Benefit)
admin.site.register(Talent)
admin.site.register(Course)
admin.site.register(Mentor)
admin.site.register(Application)
admin.site.register(Videolesson)
admin.site.register(Onlinelesson)
admin.site.register(StudentsWork)
admin.site.register(PromoCode)
