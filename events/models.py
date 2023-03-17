from __future__ import annotations
from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.query import QuerySet
from users.models import Account
import uuid


class Event(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(validators=[MinLengthValidator(10)], null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    thumbnail = models.ImageField(verbose_name="Event Thumbnail", null=True, blank=True)

    status = [
        ('upcoming', 'Upcoming'),
        ('previous', 'Previous'),
    ]
    status = models.CharField(
        max_length=20,
        choices=status,
        default="upcoming",
    )
    venue = models.CharField(max_length=100, null=True, blank=True)
    maximum_capacity = models.IntegerField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    registration = models.BooleanField(default=True)
    tags = models.ManyToManyField('Tag', blank=True)
    guests = models.ManyToManyField('users.Account', blank=True)

    class Meta:
        ordering = ['-start_date', 'title']
        verbose_name_plural = "Events"

    def __str__(self):
        return self.title

    def validate_registration(self) -> bool:
        if not self.registration:
            return False
        if not self.is_published:
            return False
        if self.status == "previous":
            return False
        return True

    @ property
    def get_thumbnail(self):
        """ Returns a thumbnail, or the default thumbnail """
        try:
            url = self.thumbnail.url
        except Exception:
            url = 'uploads/defaultEventThumbnail.jpg'
        return url

    def get_upcoming_events() -> QuerySet[Event]:
        upcoming_events = Event.objects.filter(is_published=True, status="upcoming")
        if upcoming_events.exists():
            return upcoming_events

        return None

    def get_previous_events() -> QuerySet[Event]:
        previous_events = Event.objects.filter(is_published=True, status="previous")

        if previous_events.exists():
            return previous_events

        return None

    def get_event(id: uuid) -> Event:
        event = Event.objects.get(is_published=True, id=id)

        if event:
            return event

        return None

    def get_event_tags(self):
        tags = self.tags.all()
        if tags.exists():
            return tags

        return None

    def register_guest(self, guest: Account) -> bool:
        validated = self.validate_registration()

        if validated:
            self.guests.add(guest)
            self.save()

            if self.get_total_event_guests() == self.maximum_capacity:
                self.registration = False

            return True

        return False

    def get_user_events(user: Account) -> QuerySet[Event]:
        user_events = Event.objects.filter(guests=user)

        if user_events:
            return user_events

        return None

    def get_event_guests(self) -> QuerySet[Account]:
        event_guests = self.guests.all()

        if event_guests.exists():
            return event_guests

        return None

    def get_total_event_guests(self) -> int:
        event_guests = self.guests.all()
        return event_guests.count()


class Image(models.Model):
    image = models.ImageField(verbose_name="Event Image", null=True, blank=True)
    event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE, related_name="image")

    def __str__(self):
        return f"{self.event.title} image"

    @ property
    def get_image(self):
        """ Returns a image, or the default image """
        try:
            url = self.image.url
        except Exception:
            url = 'uploads/defaultEventImage.jpg'
        return url

    def get_event_images(event: Event) -> QuerySet[Image]:
        event_images = Image.objects.filter(event=event)

        if event_images.exists():
            return event_images

        return None


class Agenda(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=150, null=True, blank=True)
    speaker = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    venue_section = models.CharField(max_length=50, null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="agenda")

    class Meta:
        ordering = ['date', 'start_time']
        verbose_name_plural = "Agendas"

    def __str__(self):
        return f"{self.title}"

    def get_event_agendas(event: Event) -> QuerySet[Agenda]:
        event_agendas = Agenda.objects.filter(event=event)
        if event_agendas.exists():
            return event_agendas

        return None


class Tag(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
