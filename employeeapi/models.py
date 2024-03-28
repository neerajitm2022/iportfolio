from django.db import models

# Create your models here.
class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    emp_code = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)