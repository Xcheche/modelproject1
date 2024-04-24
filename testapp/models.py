from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_no = models.IntegerField()
    employee_name = models.CharField(max_length=250)
    employee_salary = models.FloatField()
    employee_address = models.CharField(max_length=300)
    def __str__(self):
        return self.employee_name