from django.utils import timezone

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from employerprofile.models import Employer

# Create your models here.


class Category(models.Model):
    DELAY = (("1", "0.1"), ("2", "0.3"), ("3", "0.5"), ("4", "0.7"))
    name =models.CharField(max_length=200,null=True)
    delay = models.CharField(max_length=2, choices=DELAY,blank=True,null=True)
    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse ("jobapp:job_list", kwargs ={'name': self.name})


class Job(models.Model):
    JOB_TYPE = (("1", "Full time"), ("2", "Part time"), ("3", "Internship"))
    employer =models.ForeignKey(Employer, on_delete=models.CASCADE, null=True, blank=True)
    title =models.CharField(max_length=200)
    type = models.CharField(choices=JOB_TYPE, max_length=10)
    description=models.TextField(blank=True,null=True)
    salaryrange=models.CharField(max_length=50,blank=True,null=True)
    salary=models.IntegerField(default=0, blank=True,null=True)
    Location=models.CharField(max_length=2000, blank=True,null=True)
    category =models.ForeignKey(Category,on_delete=models.CASCADE, null=True, blank=True)
    last_date = models.DateTimeField(null=True, blank=True)
    company_name = models.CharField(max_length=100)
    company_description = models.TextField()
    website = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(default=timezone.now)
    filled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} posted by {self.employer.name}"
    
    def get_absolute_url(self):
        return reverse ("jobapp:job_details", kwargs ={'pk': self.pk})
    


class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    firstname = models.CharField(max_length=80, blank=True, null=True)
    lastname = models.CharField(max_length=80, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applicants")
    created_at = models.DateTimeField(default=timezone.now)
    comment = models.TextField(blank=True, null=True)
    status = models.SmallIntegerField(default=1)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()

    class Meta:
        ordering = ["id"]
        unique_together = ["user", "job"]

    def __str__(self):
        return f"{self.firstname} applied for {self.job.title} job"

    @property
    def get_status(self):
        if self.status == 1:
            return "Pending"
        elif self.status == 2:
            return "Accepted"
        else:
            return "Rejected"



        
