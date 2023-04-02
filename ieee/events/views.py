from django.shortcuts import redirect, render
from events.models import Event, Image, Agenda
from django.contrib.auth.decorators import login_required
from users.models import Account


def event(request, id):
    event = Event.get_event(id)
    event_images = Image.get_event_images(event)
    event_agendas = Agenda.get_event_agendas(event)

    context = {
        'event': event,
        'event_images': event_images,
        'event_agendas': event_agendas,
    }

    return render(request, 'events/event.html', context)


@login_required(login_url='login')
def event_register(request, id):
    event = Event.get_event(id)
    user = Account.get_user(request.user.id)

    if user:
        event.register_guest(user)

    return redirect('profile')
