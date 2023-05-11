from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User

# Create your models here.   

class Employer(models.Model):
    gender=(
        ('Male','male'),
        ('Female','female'),
        ('Other','other'),
    )
    username =models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name=models.CharField(max_length=200,blank=True, null=True)
    dob=models.DateField(blank=True, null=True)
    gender= models.CharField(max_length=200, blank=True, null=True, choices=gender)
    company_contact= models.CharField(max_length=200, blank=True, null=True)
    email= models.EmailField(unique=True)
    company_name =models.CharField(max_length=200,blank=True, null=True)
    company_address=models.TextField(blank=True, null=True)
    website=models.URLField(blank=True, null=True)

    def __str__(self):
        return self.username.username
