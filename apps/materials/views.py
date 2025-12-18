# apps/materials/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from apps.courses.models import Course
from apps.enrollments.models import Enrollment
from .models import Material
from .models import Material
from .forms import MaterialForm

@login_required
def instructor_materials(request, course_code):
    course = get_object_or_404(Course, code=course_code)
    materials = Material.objects.filter(course=course)

    if request.method == "POST":
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.course = course
            material.save()
            return redirect('instructor_materials', course_code=course_code)
    else:
        form = MaterialForm()

    return render(request, 'instructor/materials.html', {
        'course': course,
        'materials': materials,
        'form': form
    })
@login_required
def student_materials(request, course_id):
   
    enrollment = get_object_or_404(
        Enrollment,
        student=request.user,
        course_id=course_id,
        is_active=True
    )

    materials = Material.objects.filter(course=enrollment.course)

    return render(request, 'student/materials.html', {
        'course': enrollment.course,
        'materials': materials
    })