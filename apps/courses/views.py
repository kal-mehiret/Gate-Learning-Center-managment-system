from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/list.html', {'courses': courses})
def course_details(request, code):
    course = get_object_or_404(Course, code=code)
    return render(request, 'courses/details.html', {'course': course})
@login_required
def instructor_course_dashboard(request):
    """Instructor can see ONLY the course linked to their account"""
    course = Course.objects.filter(instructor=request.user).first()
    return render(request, 'instructor/instructor_dashboard.html', {'course': course})