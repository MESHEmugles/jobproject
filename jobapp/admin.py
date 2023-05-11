from django.contrib import admin
from .models import *
from employerprofile.models import *

# Register your models here.
admin.site.register([Category, Employer, Job, Applicant])
