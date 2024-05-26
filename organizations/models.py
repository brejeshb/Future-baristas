from django.db import models


from django.contrib.auth.models import User


# class Organization(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)


class Organization(models.Model):
    name = models.CharField(max_length=255, default=None)
    description = models.TextField(default=None)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


class Event(models.Model):
    category_choices = [
        ("conference", "Conference"),
        ("seminar", "Seminar"),
        ("workshop", "Workshop"),
        ("meetup", "Meetup"),
    ]

    category = models.CharField(max_length=50, choices=category_choices)
    name = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField()
    image = models.ImageField(upload_to="event_images/")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Add this line

    def __str__(self):
        return self.name


class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    booking_id = models.CharField(max_length=100, null=True, default="0")
    name = models.CharField(max_length=255)
    skill_set = models.CharField(max_length=255)

    def __str__(self):
        return self.name
