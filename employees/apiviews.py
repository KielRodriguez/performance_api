from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeList(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        data = EmployeeSerializer(employees, many=True).data
        return Response(data)

class EmployeeDetail(APIView):
    def get(self, request, id):
        employee = get_object_or_404(Employee, pk=id)
        data = EmployeeSerializer(employee, many=False).data
        return Response(data)



