from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from apps.courses.models import Course
from .models import Assignment
from .forms import AssignmentForm

@login_required
def instructor_assignments(request, course_code):
    course = get_object_or_404(Course, code=course_code)
    assignments = Assignment.objects.filter(course=course)

    if request.method == "POST":
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.course = course
            assignment.save()
            return redirect('instructor_assignments', course_code=course.code)
    else:
        form = AssignmentForm()

    return render(request, 'instructor/assignments.html', {
        'course': course,
        'assignments': assignments,
        'form': form
    })
from apps.enrollments.models import Enrollment

@login_required
def student_assignments(request, course_id):
    enrollment = get_object_or_404(
        Enrollment,
        student=request.user,
        course_id=course_id,
        is_active=True
    )

    assignments = Assignment.objects.filter(course=enrollment.course)

    return render(request, 'student/assignments.html', {
        'course': enrollment.course,
        'assignments': assignments
    })
