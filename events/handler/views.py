from django.shortcuts import render
from handler.models import Event, Place
from datetime import datetime, timedelta


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
