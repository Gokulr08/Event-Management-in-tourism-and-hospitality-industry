from django import forms
from .models import Contact, CustomUser
class ContactForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}))
    subject=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the subject'}))
    message=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the message'}))
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }

from django.contrib.auth.forms import UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2')
        
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match.")
        return cleaned_data

from .models import Eventt
class EventtForm(forms.ModelForm):
    class Meta:
        model = Eventt
        fields = ['title', 'description', 'location', 'venue', 'date', 'message']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter event title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter event description'}),
            'location': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select event location'}),
            'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select event venue'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local', 'placeholder': 'Select event date and time'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter any additional messages or notes'}),
        }

from .models import Registration
class RegistrationForm(forms.ModelForm):
    ticket_quantity = forms.IntegerField(min_value=1)

    class Meta:
        model = Registration
        fields = ['ticket_quantity']




