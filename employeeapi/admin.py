from django.contrib import admin
from . models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
   list_display = ('full_name','emp_code', 'mobile')
   class Meta:
        ordering = "name"
admin.site.register(Employee, EmployeeAdmin)
