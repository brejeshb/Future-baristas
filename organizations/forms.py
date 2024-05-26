from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm


class OrganizationRegistrationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ["name", "description"]


class ParticipantRegistrationForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ["name", "skill_set", "booking_id"]
        widgets = {"booking_id": forms.HiddenInput()}


class OrganizationLoginForm(AuthenticationForm):
    pass


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "category",
            "name",
            "venue",
            "date",
            "start_time",
            "end_time",
            "description",
            "image",
        ]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "start_time": forms.TimeInput(attrs={"type": "time"}),
            "end_time": forms.TimeInput(attrs={"type": "time"}),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter key points. AI will generate the rest.",
                }
            ),
        }
