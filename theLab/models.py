from django.db import models

# Create your models here.

class Courses(models.Model):
    courseID=models.CharField(max_length=9, primary_key=True)

    def __str__(self):
        return self.courseID

    
class Students(models.Model):
    studentName=models.CharField(max_length=64)
    studentID=models.IntegerField(primary_key=True)
    studentGPA=models.FloatField(max_length=3)
    studentPhoneNumber=models.IntegerField()
    courses = models.ManyToManyField(Courses, blank=True, related_name="student_courses")

    def __str__(self):
        return self.studentName


