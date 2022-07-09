from django.urls import path

from employees.apiviews import EmployeeList, EmployeeDetail

urlpatterns = [
    path('employees/', EmployeeList.as_view(), name='employee_list'),
    path('employees/<int:id>', EmployeeDetail.as_view(), name='employee_detail'),
]