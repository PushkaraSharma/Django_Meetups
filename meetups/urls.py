from django.urls import path
from . import views

urlpatterns = [
    path('meetups/', views.index, name="all_meetups"),
    path('meetups/<slug:meetup_slug>/success', views.registration_success, name="registration_success"),
    path('meetups/<slug:meetup_slug>', views.meetup_details, name="meetup_details")
    
]