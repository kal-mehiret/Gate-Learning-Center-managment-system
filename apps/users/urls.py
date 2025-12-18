from django.urls import path
from .views import (
    CustomLoginView, CustomLogoutView, home,
    admin_dashboard, instructor_dashboard, student_dashboard
)

urlpatterns = [
    path('', home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    
    path('instructor/dashboard/', instructor_dashboard, name='instructor_dashboard'),
    path('student/dashboard/', student_dashboard, name='student_dashboard'),
]

