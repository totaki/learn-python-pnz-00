import pytest
from rest_framework.authtoken.models import Token


@pytest.mark.django_db
def test_get_event(req):
    response = req('get', '/api/v1/public/events/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_place(req, place_data):
    response = req('post', '/api/v1/public/places/', place_data)
    data = response.json()
    assert data['place_name'] == place_data['place_name']
    assert response.status_code == 201


@pytest.mark.django_db
def test_post_event(req, event_data):
    response_set = req('post', '/api/v1/public/events/', event_data)
    assert response_set.status_code == 201


@pytest.mark.django_db
def test_get_tags(req, tag):
    response = req('get', '/api/v1/public/tags/')
    data = response.json()
    assert response.status_code == 200
    assert data['results'][0]['title'] == tag.title


@pytest.mark.django_db
def test_auth(req, user):
    response_set = req('get', '/api/v1/private/places')
    assert response_set.status_code == 401
    token = Token.objects.create(user=user.user)
    response_set = req('get', '/api/v1/private/places', token=token)
    assert response_set.status_code == 200


@pytest.mark.django_db
def test_create_place(auth_req, place_data):
    response_set = auth_req('post', '/api/v1/private/places', body=place_data)
    assert response_set.status_code == 201
    data = response_set.json()
    assert data['place_name'] == place_data['place_name']
    assert data['owner'] == 1


@pytest.mark.django_db
def test_create_event(auth_req, private_event_data):
    response_set = auth_req('post', '/api/v1/private/events', body=private_event_data)
    assert response_set.status_code == 201
    data = response_set.json()
    assert data['title'] == private_event_data['title']
