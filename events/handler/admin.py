from django.contrib import admin

from .models import Event, Place, Tag, User, Notification


admin.site.register(Event)
admin.site.register(Tag)
admin.site.register(Place)
admin.site.register(User)
admin.site.register(Notification)
