from django.contrib import admin
from .models import Company, Employee
from .modelsAdminView import CompanyAdminView, EmployeeAdminView


admin.site.register(Company, CompanyAdminView)
admin.site.register(Employee, EmployeeAdminView)
