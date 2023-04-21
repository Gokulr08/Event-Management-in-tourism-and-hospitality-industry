from django.contrib import admin
from django.contrib.admin.models import LogEntry, DELETION
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from .models import Contact, CustomUser, Registration, Venue, Organizer, ContactPerson, Schedule, Event, Eventt, Location

admin.site.register(Venue)
admin.site.register(Organizer)
admin.site.register(ContactPerson)
admin.site.register(Schedule)
admin.site.register(Event)
admin.site.register(Contact)
admin.site.register(CustomUser)
admin.site.register(Eventt)
admin.site.register(Location)
admin.site.register(Registration)