from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student

def home(request):
    if request.method == "POST":
        # Get data from form
        name = request.POST.get("name")
        email = request.POST.get("email")
        website = request.POST.get("website")
        description = request.POST.get("description")
        gender = request.POST.get("gender")
        roll = request.POST.get("roll")
        age = request.POST.get("age")
        edu_cost = request.POST.get("edu_cost")
        semester_cost = request.POST.get("semester_cost")
        is_married = True if request.POST.get("is_married") == "on" else False
        birth_date = request.POST.get("birth_date")
        class_time = request.POST.get("class_time")
        ass_submit = request.POST.get("ass_submit")

        # Get uploaded files
        image = request.FILES.get("image")
        resume = request.FILES.get("resume")

        # Save to database
        student = Student.objects.create(
            name=name,
            email=email,
            website=website,
            description=description,
            gender=gender,
            roll=roll,
            age=age,
            edu_cost=edu_cost,
            semester_cost=semester_cost,
            is_married=is_married,
            birth_date=birth_date,
            class_time=class_time,
            ass_submit=ass_submit,
            image=image,
            resume=resume
        )

        messages.success(request, f"Student {student.name} added successfully!")
        return redirect("home")  # redirect back to the same page or another page

    return render(request, "index.html")
