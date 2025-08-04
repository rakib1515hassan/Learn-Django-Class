from django.db import models

# Create your models here.
class Student(models.Model):
    class GenderType(models.TextChoices):
        MALE    = 'Male', 'male'
        FEMALE  = 'Female', 'female'
        OTHERS  = 'Others', 'others'

    name  = models.CharField(max_length=250)
    email = models.EmailField(max_length=300, unique=True)
    age   = models.PositiveIntegerField()
    roll  = models.IntegerField()
    student_class = models.CharField(max_length=250)
    dob   = models.DateField()
    image = models.ImageField(upload_to="StudentImage/", null=True, blank=True)
    gender = models.CharField(choices=GenderType.choices, max_length=10)
    

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}"