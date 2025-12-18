from django.contrib import admin
from .models import Grade


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('course', 'student', 'score', 'graded_at')
    list_filter = ('course',)
    search_fields = ('student__username', 'course__code')