import pytest
from rest_framework.test import APIClient
from handler.models import Place, Event, Tag


@pytest.fixture
def req():
    client = APIClient()

    def _(method, url, body=None):
        return getattr(client, method)(url, body, format='json')
    return _


@pytest.fixture
def place_data():
    return {
        "place_name": 'Heror',
        "city": "Penza",
        "street": "Zlobina",
        "house_number": "19",
        "office_number": 0
    }


@pytest.fixture
def place(place_data):
    return Place.objects.create(**place_data)


@pytest.fixture
def event_data(req, place):
    place_response = req('get', f'/api/v1/public/places/{place.id}/')
    place_id = place_response.json()['id']
    return {
            "title": "КиШ",
            "place": place_id,
            "body": "Князь без Горшка",
            "event_time": "2020-01-13T21:00:00Z"
    }


@pytest.fixture
def event(event_data, place):
    event_data['place'] = place
    return Event.objects.create(**event_data)


@pytest.fixture
def tag():
    tag = {
     "title": "Народная"
    }
    return Tag.objects.create(**tag)

