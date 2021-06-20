from django.contrib import admin
from .models import Location, Meetup, Participants

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title','date','location')
    list_filter = ('date','location')
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Meetup,MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participants)
