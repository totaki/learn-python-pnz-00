from django.test import TestCase
from handler.models import Event, Place
from scheduler.save_event import save_event


class SaveEventTestCase(TestCase):
    def setUp(self):
        self.events = [{
            'title': "Король Вечного Сна",
            'body': "Трибьют группы Король и Шут",
            'event_time': "2020-01-06 19:00:00",
            'place_name': "FrauGross",
            'city': "Пенза",
            'street': "Пр-кт Строителей",
            'house_number': "152 Б",
            'office_number': 4
        }]
        save_event(self.events)

    def test_save_event(self):
        """Тест записи в базу функцией save_event и чтения записанных данных из базы"""

        event = Event.objects.get(title='Король Вечного Сна')
        place = Place.objects.get(place_name='FrauGross')
        self.assertEqual(event.body, 'Трибьют группы Король и Шут')
        self.assertEqual(place.street, 'Пр-кт Строителей')

    def test_dont_save_duplicate_event(self):
        """Тест проверки на дублирование записи. При попытке записи имеющегося в базе события,
        функция save_event возвращает пустой список."""

        self.assertEqual(save_event(self.events), [])
