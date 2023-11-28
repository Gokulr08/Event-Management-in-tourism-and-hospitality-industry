from django.conf import Settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(_('phone number'), max_length=20, blank=True, null=True)
    full_name = models.CharField(_('full name'), max_length=100, blank=True)
    
    def __str__(self):
        return f"{self.full_name} ({self.email})"
    
    def save(self, *args, **kwargs):
        self.full_name = f"{self.first_name} {self.last_name}"
        super().save(*args, **kwargs)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Venue(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200,  blank=True, null=True)
    capacity = models.IntegerField( blank=True, null=True)

    def __str__(self):
        return self.name



class Organizer(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


class ContactPerson(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Schedule(models.Model):

    session_name = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.session_name

class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    event_datetime = models.DateTimeField(blank=True, null=True)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    contact_person = models.ForeignKey(ContactPerson, on_delete=models.CASCADE)
    max_capacity = models.IntegerField()
    registration_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    expected_crowd_size = models.IntegerField()
    food_provided = models.BooleanField(default=False)
    promoted = models.BooleanField(default=False)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    safety_requirements = models.TextField(blank=True)
    schedule = models.ManyToManyField(Schedule, related_name='event_schedules')



    def __str__(self):
        return self.name

class Eventt(models.Model): ##event_details
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=False, null=False)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    date = models.DateTimeField()
    max_attendees = models.PositiveIntegerField()
    cost_per_person = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.title
    

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    ticket_quantity = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.full_name} - {self.event.name}'
