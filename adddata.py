from datetime import datetime
from event.models import Venue, Organizer, ContactPerson, Schedule, Event


# Create objects and save them to the database
# Creating a new venue
venue = Venue(name='Madison Square Garden', address='4 Pennsylvania Plaza, New York, NY 10001', capacity=20000)
venue.save()

# Creating a new organizer
organizer = Organizer(name='Live Nation', phone_number='555-555-5555', email='info@livenation.com')
organizer.save()

# Creating a new contact person
contact_person = ContactPerson(name='John Smith', phone_number='555-555-5555', email='john.smith@example.com')
contact_person.save()

# Creating a new schedule
schedule = Schedule(session_name='Main Stage', start_time='19:00:00', end_time='23:00:00', description='Headliners perform')
schedule.save()

# Creating a new event
event = Event(
    name='Music Festival', 
    description='A music festival featuring various artists', 
    location='Madison Square Garden', 
    event_datetime=datetime.datetime(2023, 7, 15, 12, 0, 0), 
    venue=venue, 
    organizer=organizer, 
    contact_person=contact_person, 
    max_capacity=20000, 
    registration_fee=50.00, 
    budget=1000000.00, 
    expected_crowd_size=15000, 
    food_provided=True, 
    promoted=True, 
    image='uploads/img5.jpg', 
    safety_requirements='Security personnel required at entrance', 
)
event.save()

# Adding the schedule to the event
event.schedule.add(schedule)
