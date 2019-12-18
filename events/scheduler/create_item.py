import logging
from handler.models import Event, Place, Tag
from typing import List


def save_into_db(event: List):
    keys_place = ['place_name', 'city', 'street', 'house_number', 'office_number']
    keys_event = ['title', 'place', 'event_time', 'body', 'tags']
    event_list = event[:4]
    place_list = event[4:]
    place_list = dict(zip(keys_place, place_list.values()))
    place_into_bd = Place(**place_list)
    place_into_bd.save()
    event_list = dict(zip(keys_event, event_list.values()))
    event_list['place'] = place_into_bd
    event_into_bd = Event(**event_list)
    event_into_bd.save()
    event_from_bd = Event.objects.filter(title=event_into_bd['title'])
    id_new = event_from_bd.id
    return id_new


def save_events(events: List) -> None:
    id_new_events = []
    db_events = Event.objects.all()
    for db_event in db_events:
        for some_events in events:
            for event in some_events:
                if db_event.title != event['title']:
                    id_new_events.append(save_into_db(event))
                elif db_event.event_time != event['event_time']:
                    id_new_events.append(save_into_db(event))
                else:
                    logging.error(f'Items {db_event.title} already exist')
    return id_new_events


