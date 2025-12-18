# apps/enrollments/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Enrollment

@login_required
def student_dashboard(request):
    enrollments = Enrollment.objects.filter(
        student=request.user,
        is_active=True
    ).select_related('course')

    
    return render(request, 'student/student_dashboard.html', {
        'enrollments': enrollments
    })

    