from django.db import models


# creating company model
class Company(models.Model):
    name = models.CharField(max_length=128, null=False)
    location = models.CharField(max_length=256, null=False)
    about = models.CharField(max_length=256, null=True)
    type = models.CharField(max_length=64, choices=(
        ('IT', 'IT'),
        ('Pharmaceutical', 'Pharmaceutical'),
        ('Entertainment', 'Entertainment')
    ))
    founded = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
