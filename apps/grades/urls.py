from django.urls import path
from .views import instructor_grades, student_grades,assign_grade
from . import views

urlpatterns = [
    path('instructor/grades/<str:course_code>/', instructor_grades, name='instructor_grades'),
    path('student/grades/<int:course_id>/', student_grades, name='student_grades'),
   path('assign/<int:student_id>/<int:course_id>/', assign_grade, name='assign_grade'),
]


