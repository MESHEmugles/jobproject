from datetime import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from . models import Applicant, Job, Employer


class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=15)
    first_name =forms.CharField(max_length=250)
    last_name =forms.CharField(max_length=250)
    email =forms.CharField(max_length=50)
    
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email', 'password1', 'password2']

class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ("created_at", "employer",)
        labels = {
            "last_date": "Last Date",
            "company_name": "Company Name",
            "company_description": "Company Description",
        }

    def is_valid(self):
        valid = super(CreateJobForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def clean_last_date(self):
        date = self.cleaned_data["last_date"]
        try:
            if date.date() is None:
                return date
        except:
            if date.date() < datetime.now().date():
                raise ValidationError("Last date can't be before from today")
            return date

    def save(self, commit=True):
        job = super(CreateJobForm, self).save(commit=False)
        if commit:
            job.save()
        return job


class ApplyJobForm(forms.ModelForm):

    class Meta:
        model = Applicant
        fields = ("firstname","lastname","email","resume","cover_letter",)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Employer
        
        fields = "__all__"