from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, unique=True)

    def __str__(self):
        return '{first_name} {last_name}'.format(first_name=self.user.first_name, last_name=self.user.last_name)

    class Meta:
        verbose_name_plural = "Employees"