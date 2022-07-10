from django.urls import path

from employees.apiviews import  EmployeeViewSet

employee_list = EmployeeViewSet.as_view({
    "get": "list",
    "post": "create"
})
employee_detail = EmployeeViewSet.as_view({
    "get": "retrieve",
    # "put": "update",
    "patch": "partial_update",
    # "delete": "destroy"
})

urlpatterns = [
    path('manage/employees/', employee_list, name='employee-list'),
    path('manage/employees/<int:pk>/', employee_detail, name='employee-detail'),
]