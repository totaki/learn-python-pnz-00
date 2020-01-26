import pytest
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from handler.models import Place, Event, Tag, User
from django.contrib.auth.models import User as DjangoUser


@pytest.fixture
def req():
    client = APIClient()

    def _(method, url, body=None, token=None):
        if token:
            client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
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


@pytest.fixture
def user():
    external_id = '0000000000'
    username = f'telegram_{external_id}'
    django_user = DjangoUser.objects.create(username=username)
    return User.objects.create(name='test_user', external_id=external_id, user=django_user)


@pytest.fixture
def auth_req(req, user):
    token = Token.objects.create(user=user.user)

    def _(method, url, body=None):
        return req(method, url, body, token=token)
    return _
