import pytest
from rest_framework.test import RequestsClient


@pytest.mark.django_db
def test_get_event():
    client = RequestsClient()
    response = client.get('http://localhost:8000/api/v1/events/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_place():
    client = RequestsClient()
    payload = {
        "place_name": 'Heror',
        "city": "Penza",
        "street": "Zlobina",
        "house_number": "19",
        "office_number": 0
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response_set = client.post('http://localhost:8000/api/v1/places/', json=payload, headers=headers)
    assert response_set.status_code == 201


@pytest.mark.django_db
def test_post_event():
    client = RequestsClient()
    payload = {
        "place_name": 'Heror',
        "city": "Penza",
        "street": "Zlobina",
        "house_number": "19",
        "office_number": 0
    }
    headers = {
        'Content-Type': 'application/json'
    }
    client.post('http://localhost:8000/api/v1/places/', json=payload, headers=headers)

    payload = {
        "title": "КиШ",
        "place": "http://localhost:8000/api/v1/places/1/",
        "body": "Князь без Горшка",
        "event_time": "2020-01-13T21:00:00Z"
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response_set = client.post('http://localhost:8000/api/v1/events/', json=payload, headers=headers)
    assert response_set.status_code == 201

