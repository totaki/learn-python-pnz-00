from handler.models import Event, Place
from rest_framework import serializers


class EventsSerializer(serializers.HyperlinkedModelSerializer):
    place_name = serializers.SerializerMethodField(read_only=True)
    event_date = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Event
        fields = ['title', 'place', 'body', 'event_date', 'place_name', 'event_time']

    def get_place_name(self, obj):
        return f'{obj.place.place_name}'

    def get_event_date(self, obj):
        event_date = obj.event_time.strftime("%Y.%m.%d %H:%M")
        return event_date


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class SetEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'body', 'event_time']

    def create(self, validated_data):
        """
        Create and return a new `Event` instance, given the validated data.
        """
        return Event.objects.create(**validated_data)
