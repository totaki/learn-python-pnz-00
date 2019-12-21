import logging
from handler.models import Event, Place
from typing import List

logger = logging.getLogger('__name__')


def save_event(events: List) -> List:
    id_new_events = []
    for event in events:
        try:
            place = Place.objects.get(place_name=event['place_name'])
        except Place.DoesNotExist:
            Place.objects.create(
                place_name=event['place_name'],
                city=event['city'],
                street=event['street'],
                house_number=event['house_number'],
                office_number=event['office_number']
            )
            place = Place.objects.get(place_name=event['place_name'])
        db_events = Event.objects.filter(title=event['title'], event_time=event['event_time'])
        if not db_events:
            Event.objects.create(
                title=event['title'],
                place=place,
                event_time=event['event_time'],
                body=event['body']
            )
            id_new = Event.objects.last().id
            id_new_events.append(id_new)
        else:
            logger.info("The event is in the database")
    return id_new_events


