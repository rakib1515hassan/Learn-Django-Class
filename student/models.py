from django.db import models

# Create your models here.
class Student(models.Model):
    stu_id      = models.AutoField(primary_key=True, verbose_name="Student Unique ID")
    ##? Textual Fields ----------------------------------------------------
    name        = models.CharField(max_length=100, verbose_name="Student Name")
    email       = models.EmailField(unique=True, verbose_name="Student Email")
    website     = models.URLField(null=True, blank=True, verbose_name="Portfolio Website")
    description = models.TextField(verbose_name="Description")
    
    ##? Numerical and Logical Fields ----------------------------------------------------
    roll          = models.IntegerField(verbose_name="Roll Number")
    age           = models.PositiveBigIntegerField(verbose_name="Age")
    edu_cost      = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Education Cost (per year)")
    semester_cost = models.FloatField(verbose_name="Semester Cost (per month)")
    is_married    = models.BooleanField(default=False, verbose_name="Marital Status")
    
    ##? Date and Time Fields ----------------------------------------------------
    birth_date  = models.DateField(verbose_name="Date of Birth")
    class_time  = models.TimeField(verbose_name="Class Time")
    ass_submit  = models.DateTimeField(verbose_name="Assignment Submission Time")
    
    ##? File and Image Fields ----------------------------------------------------
    image       = models.ImageField(upload_to='images/', verbose_name="Profile Image (JPG/PNG)")
    resume      = models.FileField(upload_to='files/', verbose_name="Resume (PDF/DOC/DOCX/Image/ZIP/RAR)")
    

    def __str__(self):
        return self.name