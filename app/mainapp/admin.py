from django.contrib import admin
from django.forms import ModelForm, FileField


from mainapp.models import Advantage, QuestionAnswer, Tag, Benefit, Talent, Course, Mentor, Application,\
Videolesson, Onlinelesson, StudentsWork, PromoCode, Preparation, Subscriber


admin.site.register(Advantage)
admin.site.register(QuestionAnswer)
admin.site.register(Tag)
admin.site.register(Benefit)
# admin.site.register(Talent)
admin.site.register(Mentor)
admin.site.register(Application)
admin.site.register(StudentsWork)
admin.site.register(PromoCode)
admin.site.register(Preparation)
admin.site.register(Subscriber)


# Класс-обманка для загрузки файлов .svg через алминку в модели Talent
class TalentModelForm(ModelForm):
    class Meta:
        model = Talent
        exclude = []
        field_classes = {
            'image': FileField,
        }


@admin.register(Talent)
class TalentAdmin(admin.ModelAdmin):
    list_display = 'title',
    form = TalentModelForm


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    


@admin.register(Videolesson)
class VideolessonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Onlinelesson)
class OnlinelessonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
