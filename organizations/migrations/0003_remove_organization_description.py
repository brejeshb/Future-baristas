# Generated by Django 5.0.4 on 2024-05-25 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("organizations", "0002_event"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="organization",
            name="description",
        ),
    ]
