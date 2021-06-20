from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL

class Location(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}({self.address})'


class Participants(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    organizer_email = models.EmailField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=CASCADE)
    participants = models.ManyToManyField(Participants, blank=True, null=True)

    def __str__(self):
        return f'{self.title} : {self.slug}'


