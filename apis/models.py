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

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=128, null=False)
    email = models.EmailField(max_length=128, null=False)
    address = models.CharField(max_length=256, null=False)
    contactno = models.CharField(max_length=13, null=False)
    designation = models.CharField(max_length=128, choices=(
        ('Manager', 'Project Manager'),
        ('sd', 'Software Developer'),
        ('tl', 'Technical Lead'),
        ("sse", 'Senior Software Developer'),
        ('hr', 'Human Resource'),
        ('bde', 'Business Development Executive')
    ), null=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
