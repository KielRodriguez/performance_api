from pyexpat import model
from django.db import models

from django.contrib.auth.models import User
from pkg_resources import require

# Create your models here.
class Employee(User):
    def __str__(self):
        return '{first_name} {last_name}'.format(first_name=self.first_name, last_name=self.last_name)

    class Meta:
        verbose_name_plural = "Employees"

class Review(models.Model):
    reviewer = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False, related_name="reviewer")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False, related_name="employee")
    rating = models.FloatField(max_length=5.0, null=False, default=0)
    feedback = models.TextField(max_length=300, null=True)

    def __str__(self):
        return 'rating: {}'.format(str(self.rating))