from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    meetups = [
        {'title':'1st Meetup','locations':'New York','slug':'a-first-meetup'},
        {'title':'2nd Meetup','locations':'Delhi','slug':'a-second-meetup'}
    ]
    return render(request, 'meetups/index.html',{
        'meetups':meetups,
        'show_meetups':True
        })

def meetup_details(request, meetup_slug):
    print(meetup_slug)
    selected_meetup = {
        'title':'A first Meetup',
        'description':'This meeting is basically for python developers'
    }
    return render(request, 'meetups/meetup_details.html',{
        'meetup_title':selected_meetup['title'],
        'description':selected_meetup['description']
    })        
