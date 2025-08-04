from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from app.views import home, product

from student.views import student_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
