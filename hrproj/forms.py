from django import forms
from .models import Employee, AssignDesignation, Designation

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class AssignDesignationForm(forms.ModelForm):
    employee_number = forms.ModelChoiceField(queryset=Employee.objects.all(), empty_label=None, label='Employee Number')
    designation = forms.ModelChoiceField(queryset=Designation.objects.all(), empty_label=None, label='Designation')
    
    class Meta:
        model = AssignDesignation
        fields = ['employee_number', 'designation', 'employee_type', 'status']
