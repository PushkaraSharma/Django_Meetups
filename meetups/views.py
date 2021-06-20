from meetups.forms import RegistrationForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup

# Create your views here.
def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html',{
        'meetups':meetups,
        })

def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        registration_form = RegistrationForm()
        return render(request, 'meetups/meetup_details.html',{
            'meetup_found':True,
            'meetup':selected_meetup,
            'form':registration_form
        })

    except Exception as e:
        return render(request, 'meetups/meetup_details.html',{
            'meetup_found':False
        })

