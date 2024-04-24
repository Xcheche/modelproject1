from django.contrib import admin
from testapp.models  import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_name','employee_no','employee_salary','employee_address']
    search_fields = ('employee_name','employee_no','employee_salary','employee_address',)

admin.site.register(Employee,EmployeeAdmin)
