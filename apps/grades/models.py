from django.db import models
from django.conf import settings
from apps.courses.models import Course

User = settings.AUTH_USER_MODEL

class Grade(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='grades')
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'},
        related_name='grades'
    )
    score = models.CharField(max_length=20)
    remark = models.TextField(blank=True)
    graded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('course', 'student')

    def __str__(self):
        return f"{self.course.code} - {self.student} : {self.score}"
