from django.shortcuts import render
from events.models import Event


def home(request):
    previous_events = Event.get_previous_events()
    upcoming_events = Event.get_upcoming_events()

    context = {
        'previous_events': previous_events,
        'upcoming_events': upcoming_events
    }

    return render(request, 'landing_page/index.html', context)
