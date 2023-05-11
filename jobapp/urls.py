from django.urls import path
from .views import *

app_name = 'jobapp'

urlpatterns = [
    path('',HomeView.as_view(),name='index'),
    path('register/',register,name='register_employer'),
    path('signin/',signin,name='login'),
    path('logout/',logoutuser,name='logout'),
    path('list/',JobList.as_view(),name='job_list'),
    path('details/<pk>/',JobDetails.as_view(),name='job_details'),
    path('apply/<str:id>/',apply_page,name='apply'),
]