from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.users.views import home
from apps.courses import views as course_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', course_views.course_list, name='course_list'),
    
   
    path('', include('apps.users.urls')),
    
  
    path('', include('apps.courses.urls')),
    path('', include('apps.materials.urls')),
    path('', include('apps.assignments.urls')),
    path('', include('apps.grades.urls')),
    
    
    
    path('', include('apps.enrollments.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)