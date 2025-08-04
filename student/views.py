from django.shortcuts import render

# Create your views here.
from .models import Student


def student_list(request):
    std = Student.objects.all()
    # print("-----------------------------------")
    # print("Student =", student)
    # print("-----------------------------------")
    
    data = {
        "students": std
    }
    return render(request, 'student/list.html', data)






def student_details(request):
    return render(request, 'student/details.html')