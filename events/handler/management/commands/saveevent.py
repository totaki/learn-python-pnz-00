from django.core.management.base import BaseCommand, CommandError
from handler.models import Event, Place
from typing import List

class Command(BaseCommand):
    """
    Command save event into bd
    """
    help = 'Save parsing events into BD'
    KEYS_PLACE = ['place_name', 'city', 'street', 'house_number', 'office_number']
    KEYS_EVENT = ['title', 'body', 'event_time', 'place']
    id_new_events = []

    def save_into_db(self, event: List) -> None:
        event_list = list(event.values())
        place_list = list(event.values())
        event_list = event_list[:3]
        place_list = place_list[3:]
        place_list = dict(zip(self.KEYS_PLACE, place_list))
        place_into_bd = Place(**place_list)
        place_into_bd.save()
        event_list = dict(zip(self.KEYS_EVENT, event_list))
        event_list['place'] = place_into_bd
        event_into_bd = Event(**event_list)
        event_into_bd.save()
        id_new = Event.objects.last().id
        self.id_new_events.append(id_new)

    def handle(self, events: List, *args, **options) -> int:
        for event in events:
            db_events = Event.objects.filter(title=event['title'])
            if not db_events:
                self.save_into_db(event)
            else:
                for db_event in db_events:
                    if db_event.body != event['body']:
                        self.save_into_db(event)
                    else:
                        self.stdout.write("The event is in the database")
        return self.id_new_events
