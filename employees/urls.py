from django.urls import path

from employees.apiviews import EmployeeList, EmployeeDetail, EmployeeSave, EmployeeUpdate

urlpatterns = [
    path('employees/', EmployeeList.as_view(), name='employee_list'),
    path('employees/<int:id>', EmployeeDetail.as_view(), name='employee_detail'),
    path('employees/', EmployeeSave.as_view, name='employee_save' ),
    path('employees/<int:id>', EmployeeUpdate.as_view, name='employee_update'),
]