from django.contrib import admin


class CompanyAdminView(admin.ModelAdmin):
    list_display = ['name', 'type', 'location', 'active']


class EmployeeAdminView(admin.ModelAdmin):
    list_display = ['name', 'designation', 'email', 'company']
