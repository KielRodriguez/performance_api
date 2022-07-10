# from rest_framework.views import APIView
# from rest_framework.response import Response

# from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from utils import mixins

from .models import Employee
from .serializers import EmployeeSerializer, EmployeeCreateSerializer, EmployeeUpdateSerializer

class EmployeeViewSet(viewsets.GenericViewSet, mixins.BaseGenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    queryset = Employee.objects.all()
    list_serializer_class = EmployeeSerializer
    retrieve_serializer_class = EmployeeSerializer
    create_serializer_class = EmployeeCreateSerializer
    update_serializer_class = EmployeeUpdateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, action="create")
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        response_data = serializer.data
        del response_data['password']
        return Response(
            response_data, status=status.HTTP_201_CREATED, headers=headers
        )
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial, action="update"
        )
        print(serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}
        response_data = serializer.data
        del response_data['password']
        return Response(response_data)


