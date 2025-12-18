from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model

from apps.courses.models import Course
from apps.enrollments.models import Enrollment
from .models import Grade

User = get_user_model()
@login_required
def instructor_grades(request, course_code):
    course = get_object_or_404(
        Course,
        code=course_code,
        
    )

    enrollments = Enrollment.objects.filter(
        course=course,
        is_active=True
    ).select_related('student')

    for enrollment in enrollments:
        enrollment.grade = Grade.objects.filter(
            course=course,
            student=enrollment.student
        ).first()

    return render(request, 'instructor/grades.html', {
        'course': course,
        'enrollments': enrollments
    })
@login_required
def assign_grade(request, student_id, course_id):
    course = get_object_or_404(
        Course,
        id=course_id,
        
    )

    student = get_object_or_404(
        User,
        id=student_id,
        role='student'
    )

    enrollment = get_object_or_404(
        Enrollment,
        course=course,
        student=student,
        is_active=True
    )

    grade, _ = Grade.objects.get_or_create(
        course=course,
        student=student
    )

    if request.method == "POST":
        grade.score = request.POST.get("score")
        grade.remark = request.POST.get("remark")
        grade.save()
        return redirect('instructor_grades', course_code=course.code)

    return render(request, 'instructor/assign_grade.html', {
        'course': course,
        'student': student,
        'grade': grade
    })
@login_required
def student_grades(request):
    grades = Grade.objects.filter(
        student=request.user
    ).select_related('course')

    return render(request, 'student/grades.html', {
        'grades': grades
    })
@login_required
def student_grades(request, course_id):  
    course = get_object_or_404(Course, id=course_id)
    
    
    grades = Grade.objects.filter(
        student=request.user,
        course=course  
    ).select_related('course')

    return render(request, 'student/grades.html', {
        'grades': grades,
        'course': course  
    })