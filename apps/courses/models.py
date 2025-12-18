# apps/courses/models.py
from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Course(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    
    image = models.ImageField(upload_to='courses/icons/', blank=True, null=True)
    
    instructor = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        limit_choices_to={'role': 'instructor'},
        related_name='course'
    )
    
    
    duration = models.CharField(max_length=100, blank=True, null=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    instructor = models.CharField(max_length=200)  

    def __str__(self):
        return f"{self.code} - {self.name}"