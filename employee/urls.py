from django.urls import path
from .views import EmployeesData, Employee


urlpatterns = [
    path('employeesData/', EmployeesData.as_view()),
    path('employee/<int:pk>', Employee.as_view()),
]