from django.db import models

from employees.models import Employee

# Create your models here.


class Review(models.Model):
    reviewer = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False, related_name="reviewer")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False, related_name="employee")
    rating = models.FloatField(max_length=5.0, null=False, default=0)
    feedback = models.TextField(max_length=300, null=True)

    def __str__(self):
        return 'rating: {}'.format(str(self.rating))