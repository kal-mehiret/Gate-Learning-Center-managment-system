from django.urls import path
from .views import instructor_materials, student_materials

urlpatterns = [
    path('instructor/materials/<str:course_code>/', instructor_materials, name='instructor_materials'),
    path('student/materials/<int:course_id>/', student_materials, name='student_materials'),
]
