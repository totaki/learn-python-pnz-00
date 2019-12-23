from django.test import TestCase
from handler.models import Event, Place
from scheduler.save_event import save_event


class SaveEventTestCase(TestCase):
    def setUp(self):
        event = [{
            'title': "Король Вечного Сна",
            'body': "Трибьют группы Король и Шут",
            'event_time': "2020-01-06 19:00:00",
            'place_name': "FrauGross",
            'city': "Пенза",
            'street': "Пр-кт Строителей",
            'house_number': "152 Б",
            'office_number': 4
        }]
        save_event(event)

    def test_save_event(self):
        """Events"""

        event = Event.objects.get(title='Король Вечного Сна')
        place = Place.objects.get(place_name='FrauGross')
        self.assertEqual(event.body, 'Трибьют группы Король и Шут')
        self.assertEqual(place.street, 'Пр-кт Строителей')
