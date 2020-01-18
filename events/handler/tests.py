import pytest


@pytest.mark.django_db
def test_get_event(req, event):
    response = req('get', '/api/v1/events/')
    data = response.json()
    assert response.status_code == 200
    assert data['results'][0]['title'] == event.title


@pytest.mark.django_db
def test_post_place(req, place_data):
    response = req('post', '/api/v1/places/', place_data)
    data = response.json()
    assert data['place_name'] == place_data['place_name']
    assert response.status_code == 201


@pytest.mark.django_db
def test_post_event(req, event_data):
    response_set = req('post', '/api/v1/events/', event_data)
    assert response_set.status_code == 201
