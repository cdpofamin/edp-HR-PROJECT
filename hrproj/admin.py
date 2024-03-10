from django.contrib import admin
from .models import Employee, assignDesignation, Designation, Department

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee_number', 'firstname', 'middlename', 'lastname', 'addressln', 'baranggay', 'city', 'province', 'zipcode']

admin.site.register(Employee, EmployeeAdmin)

class AssignDesignationAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee_number', 'designation_id', 'employee_type', 'status']

admin.site.register(assignDesignation, AssignDesignationAdmin)

class DesignationAdmin(admin.ModelAdmin):
    list_display = ['designation_id', 'designation_name', 'department_id', 'status']

admin.site.register(Designation, DesignationAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_id', 'department_name', 'status']

admin.site.register(Department, DepartmentAdmin)
