from django.shortcuts import render,redirect
from .models import *

from django.views.generic import ListView, DetailView, View
from django.contrib.auth import login,logout,authenticate
from .forms import *
from dataclasses import dataclass

@dataclass
class G:
    employer = Employer.objects
    jobcategory = Category.objects
    job = Job.objects
    applicant = Applicant.objects


# Create your views here.
class HomeView(View):
    template_name = 'home/index.html'
    jb = G.job.all().order_by('-id')[:3]
    categories = G.jobcategory.all()
    
    
    def get(self, request):
        cat = self.categories
        job = self.jb
        return render(request, self.template_name, {"cat": cat, "job":job})

######################### Authentication ##############################

def register(request):
    form = SignupForm()
    if request.method=="POST":
        form= SignupForm(request.POST)
        comp_name = request.POST.get("company_name")
        comp_contact = request.POST.get("company_contact")
        website = request.POST.get("website")
        if form.is_valid():            
            empuser =form.save()
            emp=G.employer.create( username = empuser, company_name = comp_name, 
                     company_contact = comp_contact, website =  website)
            emp.save()
            login(request, empuser)
            return redirect('jobapp:index')
        else:
            return redirect('jobapp:register_employer')
            
    return render(request, 'auth/register_employer.html', {'form': form})


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)
            return redirect('jobapp:index')
        else:
            return redirect('jobapp:login')

    return render(request, "auth/login.html")

def logoutuser(request):
    logout(request)
    return redirect('jobapp:login')      

############################### END OF AUTHENTICATION ##################################


############################### JOB ##################################
class JobDetails(DetailView):
    template_name = "pages/job_details.html"
    model= Job

class JobList(ListView):
    template_name= "pages/job_list.html"
    model = Job


def apply_page(request,id):
    jobdetails = G.job.get(pk=id)
    form=ApplyJobForm( instance= jobdetails )
    if request.method=='POST':
        form=ApplyJobForm(request.POST, request.FILES , instance= jobdetails)
        if form.is_valid():
            form.save()
            new = Applicant(job= G.job.get(pk=id),
                                firstname=form.cleaned_data['firstname'], 
                                lastname=form.cleaned_data['lastname'], 
                    email=form.cleaned_data['email'], resume=form.cleaned_data['resume'],
                    cover_letter=form.cleaned_data['cover_letter'] 
                    )
            new.save()
            
            return redirect('jobapp:index')
    return render(request,'pages/apply.html',{'form':form})

############################### JOB END ##################################
