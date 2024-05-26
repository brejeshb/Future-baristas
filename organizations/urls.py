from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path(
        "register/organization/",
        views.register_organization,
        name="register_organization",
    ),
    path("register/participant/", register_participant, name="register_participant"),
    path("", views.index, name="index"),
    path("create/", views.create_event, name="create_event"),
    path("success/", views.event_success, name="event_success"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("my-events/", views.my_events, name="my_events"),
    path(
        "events/<int:event_id>/participants/",
        event_participants,
        name="event_participants",
    ),
    path("all-events/", all_events, name="all_events"),
    path(
        "participate-event/<int:event_id>/",
        views.participate_event,
        name="participate_event",
    ),
    path(
        "events/<int:event_id>/participants/",
        views.event_participants,
        name="event_participants",
    ),
]
