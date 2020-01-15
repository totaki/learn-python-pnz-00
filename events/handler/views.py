from django.shortcuts import render
from handler.models import Event, Place
from datetime import datetime, timedelta
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response

from handler.serializers import EventsSerializer, PlaceSerializer


def index(request):
    start_date = datetime.utcnow()
    end_date = start_date + timedelta(days=365)
    event_list = Event.objects.filter(event_time__range=(start_date, end_date))
    context = {'event_list': event_list}
    return render(request, 'handler/index.html', context)


def place(request):
    place_list = Place.objects.all()
    context = {'place_list': place_list}
    return render(request, 'handler/place.html', context)


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventsSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


# class SetEventView(viewsets.ModelViewSet):
#     queryset = Event.objects.all()
#     serializer_class = SetEventsSerializer
#



