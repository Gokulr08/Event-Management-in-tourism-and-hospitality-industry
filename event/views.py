import datetime
from django.conf import Settings, settings
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import RegistrationForm
User = get_user_model()
from event.forms import ContactForm
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from datetime import datetime


def home(request):
    promoted_events = Event.objects.filter(promoted=True)
    context = {
        'promoted_events': promoted_events
    }
    return render(request, 'tour/index.html', context)


def eventdetail(request, ename):
    event = get_object_or_404(Event, name=ename, promoted=True)
    return render(request, 'tour/eventdetail.html', {'event': event})

def service(request):
   return render(request, 'tour/service.html')
from .forms import EventtForm

def registerevent(request):
    if request.method == 'POST':
        form = EventtForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.max_attendees = 0  # Set default value
            event.save()
            messages.success(request, 'Event created successfully.')
            return HttpResponseRedirect(reverse('event_success', args=[event.id]))

        else:
            messages.error(request, 'Error creating event. Please check your input.')
    else:
        form = EventtForm()

    context = {
        'form': form
    }

    return render(request, 'tour/registerevent.html', context)

def event_success(request, event_id):
    event = get_object_or_404(Eventt, id=event_id)

    context = {
        'event': event
    }

    return render(request, 'tour/event_success.html', context)

def aboutus(request):
   return render(request, 'tour/aboutus.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            contact = Contact(name=form.cleaned_data['name'],
                              email=form.cleaned_data['email'],
                              message=form.cleaned_data['message'],
                              timestamp=datetime.now())
            contact.save()

            # Set a success message and redirect to the success page
            messages.success(request, 'Your message was sent successfully!')
            return redirect('contact_success')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'tour/contact.html', context)

def contact_success(request):
    return render(request, 'tour/contact_success.html')

def terms(request):
    return render(request, 'tour/terms.html')

def faqs(request):
    return render(request, 'tour/faqs.html')

def eventlist(request):
    promoted_events = Event.objects.filter(promoted=True)
    context = {
        'promoted_events': promoted_events
    }
    return render(request, 'tour/eventlist.html', context)

def logout_page(request):
   if request.user.is_authenticated:
      logout(request)
      messages.success(request,"Logged out Successfully")
   return redirect("/")

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email # set email as username
            user.save()
            messages.success(request, 'Account created successfully!...You can login now')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'tour/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') # redirect to your app's home page
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'tour/login.html')



from event.models import CustomUser

@login_required
def profile(request):
    custom_user = CustomUser.objects.get(pk=request.user.pk)
    full_name = custom_user.full_name
    phone_number = custom_user.phone_number
    email = custom_user.email
    return render(request, 'tour/profile.html', {'full_name': full_name, 'phone_number': phone_number, 'email': email})
    
@login_required
def eventsuccess(request, event_id):
    event = get_object_or_404(Eventt, pk=event_id)
    email = None
    if request.user.is_authenticated:
        user = User.objects.get(pk=request.user.pk)
        email = user.email
    return render(request, 'tour/eventsuccess.html', {'event': event, 'email': email})

def event_detail(request, ename):
    event = get_object_or_404(Event, name=ename, promoted=True)
    return render(request, 'tour/eventdetail.html', {'event': event})

@login_required
def eventregistration(request, ename):
    event = get_object_or_404(Event, name=ename, promoted=True)

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            ticket_quantity = form.cleaned_data['ticket_quantity']
            total_amount = event.registration_fee * ticket_quantity
            registration = form.save(commit=False)
            registration.event = event
            registration.user = request.user
            registration.total_amount = total_amount
            registration.save()
            return redirect('eventsuccess', registration_id=registration.id)

    else:
        form = RegistrationForm()

    context = {
        'event': event,
        'form': form,
    }
    return render(request, 'tour/eventregistration.html', context)

def eventsuccess(request, registration_id):
    registration = get_object_or_404(Registration, id=registration_id)
    context = {
        'registration': registration,
    }
    return render(request, 'tour/eventsuccess.html', context)


