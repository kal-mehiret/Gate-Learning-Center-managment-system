# apps/materials/models.py
from django.db import models
from apps.courses.models import Course


class Material(models.Model):
    MATERIAL_TYPES = (
        ('pdf', 'PDF'),
        ('ppt', 'PowerPoint'),
        ('doc', 'Document'),
        ('other', 'Other'),
    )
    
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='materials'
    )
    title = models.CharField(max_length=255)
    material_type = models.CharField(max_length=20, choices=MATERIAL_TYPES)
    file = models.FileField(upload_to='courses/materials/')
    description = models.TextField(blank=True)
    
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.course.code} - {self.title}"