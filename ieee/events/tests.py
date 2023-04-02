from django.test import TestCase
from events.models import Event, Tag, Agenda
from django.db.models.query import QuerySet
from django.contrib.auth import get_user_model

from users.models import Account


class EventTest(TestCase):

    def setUp(self):
        Event.objects.create(title="IEEE XP", description="Programming", status="previous", is_published=True)
        pj_event = Event.objects.create(title="PJ", description="Programming Jam", status="upcoming", is_published=True)
        Event.objects.create(title="CCIS Open Day", description="Open Day", status="upcoming", is_published=True, maximum_capacity=1)
        Event.objects.create(title="Java Tutorials", description="Java Tutorials", status="upcoming", is_published=True)
        oracle_event = Event.objects.create(title="Oracle", description="visit", status="previous", is_published=True)

        visit_tag = Tag.objects.create(name="Visit")
        trip_tag = Tag.objects.create(name="Trip")

        user_1 = Account.objects.create_user(username='bahaa', password='DevOps')
        user_2 = Account.objects.create_user(username='noor', password='DevOps2')
        Account.objects.create_user(username='noevents', password='DevOps2')

        oracle_event.guests.add(user_1)
        oracle_event.guests.add(user_2)
        oracle_event.tags.add(visit_tag)
        oracle_event.tags.add(trip_tag)

        pj_event.guests.add(user_1)

        Agenda.objects.create(title="Oracle Stack", event=oracle_event)

    def test_previous_events_exists(self):
        response = Event.get_previous_events()

        # Return type:
        self.assertEqual(type(response), QuerySet)
        self.assertEqual(response.model, Event)

        # Expected values:
        self.assertEqual(response.count(), 2)
        for event in response:
            self.assertEqual(event.status, "previous")

    def test_upcoming_events_exists(self):
        response = Event.get_upcoming_events()

        # Return type:
        self.assertEqual(type(response), QuerySet)
        self.assertEqual(response.model, Event)

        # Expected values:
        self.assertEqual(response.count(), 3)
        for event in response:
            self.assertEqual(event.status, "upcoming")

    def test_previous_events_none(self):
        Event.objects.all().delete()
        response = Event.get_previous_events()

        # Return type:
        self.assertIsNone(response)

    def test_upcoming_events_none(self):
        Event.objects.all().delete()
        response = Event.get_upcoming_events()
        # Return type:
        self.assertIsNone(response)

    def test_get_user_events_exists(self):
        user = Account.get_user("bahaa")
        response = Event.get_user_events(user)

        # Return type:
        self.assertEqual(type(response), QuerySet)
        self.assertEqual(response.model, Event)

        # Expected values:
        self.assertEqual(response.count(), 2)
        self.assertEqual(response[0].title, "Oracle")
        self.assertEqual(response[1].title, "PJ")

    def test_get_user_events_none(self):
        user = Account.get_user("noevents")
        response = Event.get_user_events(user)
        # Return :
        self.assertIsNone(response)

    def test_get_event_guests_exists(self):
        oracle_event = Event.objects.get(title="Oracle")
        response = oracle_event.get_event_guests()

        # Return type:
        self.assertEqual(type(response), QuerySet)
        self.assertEqual(response.model, Account)

        # Expected values:
        self.assertEqual(response.count(), 2)
        self.assertEqual(response[0].username, "bahaa")
        self.assertEqual(response[1].username, "noor")

    def test_get_event_guests_none(self):
        oracle_event = Event.objects.get(title="Java Tutorials")
        response = Event.get_event_guests(oracle_event)
        # Return:
        self.assertIsNone(response)

    def test_get_total_event_guests(self):
        oracle_event = Event.objects.get(title="Oracle")
        response = oracle_event.get_total_event_guests()

        # Return type:
        self.assertEqual(type(response), int)

        # Expected values:
        self.assertEqual(response, 2)

    def test_register_guest_valid(self):
        user = Account.get_user("bahaa")
        ccis_event = Event.objects.get(title="CCIS Open Day")
        validation = ccis_event.validate_registration()
        response = ccis_event.register_guest(user)

        # Return type:
        self.assertTrue(response)
        self.assertTrue(validation)

        # Expected values:
        self.assertEqual(ccis_event.get_total_event_guests(), 1)

    def test_register_guest_invalid(self):
        user_1 = Account.get_user("bahaa")
        user_2 = Account.get_user("noor")
        ccis_event = Event.objects.get(title="CCIS Open Day")
        ccis_event.register_guest(user_1)
        validation = ccis_event.validate_registration()

        response = ccis_event.register_guest(user_2)

        # Return type:
        self.assertFalse(validation)
        self.assertFalse(response)

        # Expected values:
        self.assertEqual(ccis_event.get_total_event_guests(), 1)
