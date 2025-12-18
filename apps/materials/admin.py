from django.contrib import admin
from .models import Material


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'material_type', 'uploaded_at')
    list_filter = ('material_type', 'course')
    search_fields = ('title', 'course__code')