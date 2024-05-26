from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import *
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Organization
from django.contrib import messages
from .decorators import unauthenticated_user
from .models import Event, Participant
from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect


@login_required
def participate_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    # Add the current user as a participant to the event
    participant, created = Participant.objects.get_or_create(
        event=event, user=request.user
    )
    if created:
        messages.success(
            request, f"You've successfully registered for the event: {event.name}"
        )
    else:
        messages.info(request, f"You're already registered for the event: {event.name}")
    return redirect("all_events")


@login_required
def all_events(request):
    events = Event.objects.all()
    user_participations = Participant.objects.filter(user=request.user).values_list(
        "event_id", flat=True
    )
    context = {"all_events": events, "user_participations": user_participations}
    return render(request, "organizations/all_events.html", context)


@login_required
def my_events(request):
    # Get all events created by the user (if applicable)
    user_events = Event.objects.filter(user=request.user)

    # Get all events the user has joined
    user_participations = Participant.objects.filter(user=request.user).select_related(
        "event"
    )

    context = {
        "user_events": user_events,
        "user_participations": user_participations,
    }
    return render(request, "organizations/my_events.html", context)


@unauthenticated_user
def register_organization(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        organization_form = OrganizationRegistrationForm(request.POST)
        if user_form.is_valid() and organization_form.is_valid():
            # Create a new user
            new_user = user_form.save()
            # Create a new organization associated with the user
            new_organization = organization_form.save(commit=False)
            new_organization.user = new_user  # Link the organization to the new user
            new_organization.save()
            # Log in the new user
            login(request, new_user)
            messages.success(request, "Registration successful!")
            return redirect("index")
        else:
            messages.error(
                request, "Registration failed. Please correct the errors below."
            )
    else:
        user_form = UserCreationForm()
        organization_form = OrganizationRegistrationForm()
    return render(
        request,
        "organizations/register.html",
        {"user_form": user_form, "organization_form": organization_form},
    )


@unauthenticated_user
def register_participant(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        participant_form = ParticipantRegistrationForm(request.POST)
        if user_form.is_valid() and participant_form.is_valid():
            # Create a new user
            new_user = user_form.save()
            # Create a new participant associated with the user
            participant = participant_form.save(commit=False)
            participant.user = new_user  # Link the participant to the new user
            participant.save()
            # Log in the new user
            login(request, new_user)
            messages.success(request, "Registration successful!")
            return redirect("index")
        else:
            messages.error(
                request, "Registration failed. Please correct the errors below."
            )
    else:
        user_form = UserCreationForm()
        participant_form = ParticipantRegistrationForm()
    return render(
        request,
        "organizations/register-participant.html",
        {"user_form": user_form, "participant_form": participant_form},
    )


# def register_participant(request):
#     if request.method == "POST":
#         user_form = UserCreationForm(request.POST)
#         participant_form = ParticipantRegistrationForm(request.POST)
#         if user_form.is_valid() and participant_form.is_valid():
#             # Create a new user
#             new_user = user_form.save()
#             # Create a new participant associated with the user
#             participant = participant_form.save(commit=False)
#             participant.user = new_user  # Link the participant to the new user
#             participant.save()
#             messages.success(request, "Registration successful!")
#             return redirect("index")
#         else:
#             messages.error(
#                 request, "Registration failed. Please correct the errors below."
#             )
#     else:
#         user_form = UserCreationForm()
#         participant_form = ParticipantRegistrationForm()
#     return render(
#         request,
#         "organizations/register-participant.html",
#         {"user_form": user_form, "participant_form": participant_form},
#     )


class CustomLoginView(LoginView):
    template_name = "organizations/login.html"  # Your login template
    authentication_form = OrganizationLoginForm
    success_url = reverse_lazy("index")


def index(request):
    return render(request, "organizations/index.html")


@login_required
def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new event object from the form data
            event = form.save(commit=False)
            # Associate the event with the logged-in user
            event.user = request.user
            # Save the event object
            event.save()
            return render(
                request, "organizations/event_success.html", {"form": form.cleaned_data}
            )
    else:
        form = EventForm()
    return render(request, "organizations/create_event.html", {"form": form})


def event_success(request):
    return render(request, "organizations/event_success.html")


def event_participants(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    participants = (
        event.participant_set.all()
    )  # assuming a reverse relationship named 'participant_set'
    context = {
        "event": event,
        "participants": participants,
    }
    return render(request, "organizations/event_participants.html", context)
