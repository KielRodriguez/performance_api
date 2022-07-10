from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "username", "email", "first_name", "last_name")

class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("username", "first_name", "last_name", "email", "password")

    def create(self, validated_data):
        password= validated_data.pop("password")
        user = Employee(username=validated_data.pop("username"), **validated_data)
        user.set_password(password)
        user.save()

        return user

class EmployeeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("first_name", "last_name", "email", "password")


    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data.pop("password"))

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        return instance