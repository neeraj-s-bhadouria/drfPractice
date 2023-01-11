from rest_framework import viewsets
from .models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerialzer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerialzer
