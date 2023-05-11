from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *

from jobapp.forms import *
from jobapp.views import G


# Create your views here.

############################### PROFILE ##################################
@login_required(login_url='loggin')
def profile(request):
    profile = G.employer.get(username__username= request.user.username)

    return render (request, 'pages/profile.html', {'profile': profile,})

@login_required(login_url='loggin')
def proedit(request):
    load_profile = G.employer.get(username__username= request.user.username)
    form = ProfileForm(instance=request.user.employer)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.employer)
        if form.is_valid():
            form=form.save()
            return redirect('employerprofile:profile')
        else:
           return redirect('employerprofile:profile')

    context = {
        'load_profile': load_profile,
        'form':form,
    }
    return render(request, 'pages/proedit.html', context)

############################## PROFILE END ##################################

############################## JOB CREATE AND EDIT ##################################
@login_required(login_url='loggin')
def createjob(request):
    form=CreateJobForm(instance= request.user.employer)
    if request.method=='POST':
        form=CreateJobForm(request.POST, instance= request.user.employer)
        if form.is_valid():
            form.save()
            return redirect('jobapp:job_list')
    return render(request,'job/create_job.html',{'form':form})

@login_required(login_url='loggin')
def editjob(request, pk):
    jobdetails = G.job.get(pk=pk)
    form=CreateJobForm(instance= jobdetails)
    if request.method=='POST':
        form=CreateJobForm(request.POST, instance=jobdetails)
        if form.is_valid():
            form.save()
            return redirect('jobapp:job_details', jobdetails.pk)
        
    return render(request,'job/create_job.html',{'form':form})

############################## JOB CREATE AND EDIT END ##################################

@login_required(login_url='loggin')
def listjob(request):
    list = G.job.filter(employer= request.user.employer)

    return render (request, 'job/listjob.html', {'list': list,})

