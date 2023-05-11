from django.urls import path
from .views import *

app_name = 'employerprofile'

urlpatterns = [
    path('profile/',profile,name='profile'),
    path('edit-profile/',proedit,name='proedit'),
    path('create-job/',createjob,name='create_job'),
    path('edit-job/<str:pk>/',editjob,name='create_job'),
    path('listjob/',listjob,name='listjob'),
]