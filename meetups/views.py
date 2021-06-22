from meetups.forms import RegistrationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Meetup, Participants

# Create your views here.
def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html',{
        'meetups':meetups,
        })

def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)

        if request.method == "GET":
            registration_form = RegistrationForm()
            
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participants, _ = Participants.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participants)
                return redirect('registration_success', meetup_slug=meetup_slug)
                
        return render(request, 'meetups/meetup_details.html',{
                'meetup_found':True,
                'meetup':selected_meetup,
                'form':registration_form
            })        


    except Exception as e:
        print(e)
        return render(request, 'meetups/meetup_details.html',{
            'meetup_found':False
        })


def registration_success(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration_success.html',{
        'organizer_email':meetup.organizer_email
    })    

