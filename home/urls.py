from django.urls import path, include
from .views import get_students, student_details, add_student_details

urlpatterns = [
    path('getStudents/', get_students),
    path('getStudent/<int:id>/', student_details),
    path('addStudentDetails/', add_student_details),
    # path('updateStudentDetails/<id>/', student_details),
    # path('alterStudentDetails/<id>/', student_details),
]
