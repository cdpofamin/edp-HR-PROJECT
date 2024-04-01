from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm, AssignDesignationForm
from .models import Designation, Employee
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    return render(request, 'home.html')

def employee_form(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after successful form submission
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})

def assign_designation_form(request):
    if request.method == 'POST':
        form = AssignDesignationForm(request.POST)
        if form.is_valid():
            # Get the selected designation name from the form
            designation_name = form.cleaned_data['designation']

            # Retrieve the corresponding Designation object from the database
            designation = Designation.objects.get(designation_name=designation_name)

            # Assign the numeric ID of the Designation object to the form's designation field
            form.instance.designation_id = designation.designation_id

            # Save the form
            form.save()
            return redirect('home')  # Redirect to home page after successful form submission
    else:
        form = AssignDesignationForm()
    return render(request, 'assign_designation_form.html', {'form': form})

def employee_list(request):
    # Retrieve all employees from the database
    employees = Employee.objects.all()

    # Pass the employees to the template for rendering
    return render(request, 'employee_list.html', {'employees': employees})

def view_employee(request, employee_id):
    # Retrieve the employee object from the database using the employee_id
    employee = get_object_or_404(Employee, id=employee_id)
    
    # Render the employee details template with the employee object
    return render(request, 'view_employee.html', {'employee': employee})

def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {'form': form})

def delete_employee(request, employee_id):
    # Retrieve the employee object from the database
    employee = Employee.objects.get(id=employee_id)
    
    # Delete the employee from the database
    employee.delete()
    
    # Redirect back to the employee list page
    return HttpResponseRedirect(reverse('employee_list'))
