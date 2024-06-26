from django.db import models

class Designation(models.Model):
    designation_id = models.AutoField(primary_key=True)
    designation_name = models.CharField(max_length=100)
    department_id = models.IntegerField()  # Assuming department_id is an IntegerField
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.designation_name

class Department(models.Model):
    department_id = models.AutoField(primary_key=True, default='default_value_here')  # Set your default value here
    department_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    employee_number = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    addressln = models.CharField(max_length=100)
    baranggay = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstname} {self.middlename} {self.lastname}"



class AssignDesignation(models.Model):
    id = models.AutoField(primary_key=True)   
    employee_number = models.ForeignKey(Employee, on_delete=models.CASCADE)
    designation_id = models.CharField(max_length=100, default='default_value_here') 
    employee_type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return str(self.designation_id)