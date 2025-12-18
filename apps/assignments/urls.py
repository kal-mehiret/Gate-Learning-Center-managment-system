from django.urls import path
from .views import instructor_assignments, student_assignments

urlpatterns = [
    path('instructor/assignments/<str:course_code>/', instructor_assignments, name='instructor_assignments'),
    path('student/assignments/<int:course_id>/', student_assignments, name='student_assignments'),
]
