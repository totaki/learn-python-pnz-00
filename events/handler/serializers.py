from handler.models import Event, Place
from rest_framework import serializers


class EventsSerializer(serializers.HyperlinkedModelSerializer):
    place_name = serializers.SerializerMethodField()
    event_date = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['title', 'place', 'body', 'event_date', 'place_name']

    def get_place_name(self, obj):
        return f'{obj.place.place_name}'

    def get_event_date(self, obj):
        event_date = obj.event_time.strftime("%Y.%m.%d %H:%M")
        return event_date


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
