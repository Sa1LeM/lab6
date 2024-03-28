from django.urls import path
from . import views

app_name = "sqllab"
urlpatterns = [
    path("students",views.studentsPage, name="students"),
    path("courses",views.courses, name="courses"),
    path("details/<int:studentID>",views.details, name="details"),
]