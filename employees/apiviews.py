# from rest_framework.views import APIView
# from rest_framework.response import Response

# from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import Employee
from .serializers import EmployeeSerializer, EmployeeCreateSerializer

# class EmployeeList(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         data = EmployeeSerializer(employees, many=True).data
#         return Response(data)

# class EmployeeDetail(APIView):
#     def get(self, request, id):
#         employee = get_object_or_404(Employee, pk=id)
#         data = EmployeeSerializer(employee, many=False).data
#         return Response(data)

class EmployeeList(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeSave(generics.CreateAPIView):
    serializer_class = EmployeeCreateSerializer

class EmployeeUpdate(generics.UpdateAPIView):
    serializer_class = EmployeeCreateSerializer


