from django.contrib import admin

from authapp.models import StudentUser


@admin.register(StudentUser)
class StudentUserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'phone_number', 'age', 'deleted']
    list_filter = ['created_at']
    search_fields = ['first_name', 'phone_number']
    date_hierarchy = 'created_at'
