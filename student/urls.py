from django.urls import path

from .views import student_list, student_details

urlpatterns = [
    path('list/', student_list),
    path('details/', student_details),
]