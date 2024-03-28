from django.shortcuts import render, redirect
from django import forms
from .models import Students, Courses
from django.forms import ModelForm

class StudentForm(forms.ModelForm):
    class Meta:
        model=Students
        fields="__all__"

class Courseform(forms.ModelForm):
    class Meta:
        model=Courses
        fields="__all__"

def studentsPage(request):
    students = Students.objects.all()
    form = StudentForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("sqllab:students")
    return render(request, "links/students.html", {"students":students, "form": form})

def courses(request):
    courses = Courses.objects.all()
    form = Courseform(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("sqllab:courses")
    return render(request, "links/courses.html", {"courses":courses, "form": form})


def details(request, studentID):
    if request.method == "POST":
        student=Students.objects.get(pk=studentID)
        selected_course_id = request.POST.get('course')
        course = Courses.objects.get(pk=selected_course_id)
        student.courses.add(course)
        return redirect("sqllab:details",studentID=studentID)
    else:
        student=Students.objects.get(pk=studentID)
        course=student.courses.all()
        notRegisteredCourses = Courses.objects.exclude(student_courses=student)
        return render(request, "links/details.html", {"student":student, "course":course, "notRegisteredCourses":notRegisteredCourses})
      