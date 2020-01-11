from handler.models import Event, Place
from rest_framework import serializers


class EventsSerializer(serializers.HyperlinkedModelSerializer):
    place_name = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['title', 'place', 'body', 'event_time', 'place_name']

    def get_place_name(self, obj):
        return f'This is name {obj.place.place_name}'


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
