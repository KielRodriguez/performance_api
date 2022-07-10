from django.contrib.auth.models import User

# Create your models here.
class Employee(User):
    def __str__(self):
        return '{first_name} {last_name}'.format(first_name=self.first_name, last_name=self.last_name)

    class Meta:
        verbose_name_plural = "Employees"