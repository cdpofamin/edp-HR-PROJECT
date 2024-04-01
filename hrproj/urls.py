"""
URL configuration for hrproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import edit_employee

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('employee_form/', views.employee_form, name='employee_form'),
    path('assign_designation_form/', views.assign_designation_form, name='assign_designation_form'),
    path('employee_list/', views.employee_list, name='employee_list'),  
    path('view_employee/<int:employee_id>/', views.view_employee, name='view_employee'),  # Adjusted URL pattern
    path('edit_employee/<int:employee_id>/', edit_employee, name='edit_employee'),
    path('employee/delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),
]