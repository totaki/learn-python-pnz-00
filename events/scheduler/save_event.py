import logging
from handler.models import Event, Place
from typing import List

logger = logging.getLogger('__name__')


def get_place(event):
    try:
        place = Place.objects.get(place_name=event['place_name'])
    except Place.DoesNotExist:
        place = Place.objects.create(
            place_name=event['place_name'],
            city=event['city'],
            street=event['street'],
            house_number=event['house_number'],
            office_number=event['office_number']
        )
    return place


def save_event(events: List) -> List:
    id_new_events = []
    for event in events:
        place = get_place(event)
        try:
            Event.objects.get(title=event['title'], event_time=event['event_time'])
            print(f"The event {event['title']} is in the database")
        except Event.DoesNotExist:
            new_event = Event.objects.create(
                title=event['title'],
                place=place,
                event_time=event['event_time'],
                body=event['body']
            )
            id_new_events.append(new_event.id)
    return id_new_events


