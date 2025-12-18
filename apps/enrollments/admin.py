# apps/enrollments/admin.py
from django.contrib import admin
from .models import Enrollment


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'is_active', 'enrolled_at')
    list_filter = ('is_active', 'course')
    search_fields = ('student__username', 'course__code')