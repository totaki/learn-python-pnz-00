import logging
import urllib.parse
from parsers.base_parser import BaseParser

logger = logging.getLogger(__name__)


class TimePadParser(BaseParser):

    def get_request_params(self):

        f = ['starts_at', 'name', 'description_short', 'url', 'poster_image', 'location']
        fields = ', '.join(f)
        payload = {'fields': fields, 'limit': 30, 'cities': 'Пенза'}
        params = urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
        url = 'https://api.timepad.ru/v1/events.json'
        return 'get', url, params

    def parse(self, response) -> None:
        print(type(response))
        events = response.json()
        print(type(events))
        for event in events['values']:
            try:
                title = event['name']
                body = event['description_short']
                event_time = event['starts_at']
                place_name = None
                city = event['location']['city']
                street_full = event['location']['address'].split()
                street = street_full[-2]
                house_number = street_full[-1]

                self.items.append({
                    "title": title,
                    "body": body,
                    "event_time": event_time,
                    "place_name": place_name,
                    "city": city,
                    "street": street,
                    "house_number": house_number,
                    "office_number": 0
                })

                self.items.append(response)
            except AttributeError:
                logger.error('AttributeError - Ошибка поиска по странице HTML, отсутствует тег для поиска')

