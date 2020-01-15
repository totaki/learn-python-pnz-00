import requests
import json
from django.test import TestCase
from handler.models import Event, Place, User
from scheduler.save_event import save_event


# class SaveEventTestCase(TestCase):
#     def setUp(self):
#         self.events = [{
#             'title': "Король Вечного Сна",
#             'body': "Трибьют группы Король и Шут",
#             'event_time': "2020-01-06 19:00:00",
#             'place_name': "FrauGross",
#             'city': "Пенза",
#             'street': "Пр-кт Строителей",
#             'house_number': "152 Б",
#             'office_number': 4
#         }]
#         save_event(self.events)
#
#     def test_save_event(self):
#         """Тест записи в базу функцией save_event и чтения записанных данных из базы"""
#
#         event = Event.objects.get(title='Король Вечного Сна')
#         place = Place.objects.get(place_name='FrauGross')
#         self.assertEqual(event.body, 'Трибьют группы Король и Шут')
#         self.assertEqual(place.street, 'Пр-кт Строителей')
#
#
# class SaveUserTestCase(TestCase):
#     def setUp(self):
#         User.objects.create(external_id='0001', name='Albert Einstein', creation_date='2019-12-27 13:00')
#         User.objects.create(external_id='0002', name='Max Born', creation_date='2019-12-27 13:01')
#
#     def test_user_model(self):
#         """Тест работы модели user"""
#         user_1 = User.objects.get(external_id='0001')
#         user_2 = User.objects.get(name='Max Born')
#         self.assertEqual(user_1.name, 'Albert Einstein')
#         self.assertEqual(user_2.external_id, '0002')

# class SaveEventTestCase(TestCase):
#     def setUp(self):
#         self.payload = {
#             'fields': {
#                 'title': "Король Вечного Сна",
#                 'body': "Трибьют группы Король и Шут",
#                 'event_time': "2020-01-06 19:00:00",
#             }
#         }
#         self.url = 'http://localhost:8000/api/v1/setevent/'
#
#     def test_save_event(self):
#         """Тест post запроса к серверу"""
#
#         r = requests.post(self.url, json=self.payload, headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
#         self.assertEqual(r.status_code, 200)
#
import pytest


@pytest.mark.django_db
def test_create_event():
    pass