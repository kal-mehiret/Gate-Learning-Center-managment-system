# apps/enrollments/models.py
from django.db import models
from django.conf import settings
from apps.courses.models import Course

User = settings.AUTH_USER_MODEL

class Enrollment(models.Model):
    """
    This model is the ACCESS CONTROLLER.
    If an enrollment exists, the student can see the course data.
    """
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'},
        related_name='enrollments'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    
    enrolled_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('student', 'course')
        ordering = ['-enrolled_at']
    
    def __str__(self):
        return f"{self.student} -> {self.course.code}"