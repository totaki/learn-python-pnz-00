from handler.models import Notification, User
from handler.event_bot import get_event_notificator


def get_notification_runner(token, request_kwargs):
    send = get_event_notificator(token, request_kwargs)

    def send_events(ids):
        for id in ids:
            notif_obj = Notification.objects.get(id=id)
            tags = notif_obj.event.tags.all()
            user_set = set()
            for tag in tags:
                for user in tag.user_set.all():
                    if user.id not in user_set:
                        send(user, notif_obj.event)
                        user_set.add(user.id)
            notif_obj.status_send = True
            notif_obj.save()
    return send_events
