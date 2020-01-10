from handler.models import Event, Notification


def check_event():
    ids = []
    events = Event.objects.filter(handled=False)
    for event in events:
        event.handled = True
        event.save()
        notification = Notification.objects.create(status_send=False, event=event)
        ids.append(notification.id)

    return ids
