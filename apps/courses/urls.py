# apps/courses/urls.py
from django.urls import path
from apps.materials.views import instructor_materials
from apps.courses import views as course_views
from . import views
urlpatterns = [
    path('courses/', course_views.course_list, name='course_list'),
    path(
        "course/<str:course_code>/materials/",
        instructor_materials,
        name="course_materials"
    ),
    path('<str:code>/', views.course_details, name='course_details'),
]
