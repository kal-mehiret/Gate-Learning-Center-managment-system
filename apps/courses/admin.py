from django.contrib import admin
from .models import Course
from django.utils.html import format_html

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'instructor', 'is_active', 'image_tag')
    list_filter = ('is_active',)
    search_fields = ('name', 'code', 'instructor')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px;"/>', obj.image.url)
        return "-"
    image_tag.short_description = "Course Image"
