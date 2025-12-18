from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from apps.enrollments.models import Enrollment  
from apps.courses.models import Course


class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.role == 'admin':
            return '/admin/' 
        if user.role == 'instructor':
            return '/instructor/dashboard/'
        if user.role == 'student':
            return '/student/dashboard/'
        return '/'  # fallback


class CustomLogoutView(LogoutView):
    next_page = '/login/'


def home(request):
    return render(request, "base.html")


@login_required
def admin_dashboard(request):
    
    if request.user.is_staff or request.user.is_superuser:
        return redirect('/admin/') 

@login_required
def instructor_dashboard(request):
    
    course = Course.objects.filter(code=request.user.username).first()
    return render(request, "instructor/instructor_dashboard.html", {"course": course})




@login_required
def student_dashboard(request):
    
    enrollments = Enrollment.objects.filter(
        student=request.user,
        is_active=True
    ).select_related('course')

    return render(request, "student/student_dashboard.html", {
        'enrollments': enrollments
    })