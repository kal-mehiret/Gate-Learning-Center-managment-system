from django.contrib.auth.models import AbstractUser
from django.db import models


ROLE_ADMIN = 'admin'
ROLE_INSTRUCTOR = 'instructor'
ROLE_STUDENT = 'student'

ROLE_CHOICES = (
    (ROLE_ADMIN, 'Admin'),
    (ROLE_INSTRUCTOR, 'Instructor'),
    (ROLE_STUDENT, 'Student'),
)

class User(AbstractUser):
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    
    def is_admin(self):
        return self.role == ROLE_ADMIN

    def is_instructor(self):
        return self.role == ROLE_INSTRUCTOR

    def is_student(self):
        return self.role == ROLE_STUDENT
