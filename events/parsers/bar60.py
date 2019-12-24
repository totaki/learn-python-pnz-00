import logging
from bs4 import BeautifulSoup
from parsers.base_parser import BaseParser
from datetime import datetime
from typing import Tuple

logger = logging.getLogger(__name__)

PLACE_DIR = {
    "place_name": 'Bar60',
    "city": "Penza",
    "street": "Moskovskaya",
    "house_number": "60",
    "office_number": 0
}


class BarParser(BaseParser):

    def get_request_params(self) -> Tuple[str, str, dict]:
        return 'get', 'http://bar60.ru/events', {}

    def parse(self, html: str) -> None:
        """
        Это метод должен парсить страницу и добавлять найденные events в
        items
        """

        soup = BeautifulSoup(html, 'lxml')
        divs = soup.find_all('div', class_='blog-event')
        for div in divs:
            try:
                title = div.find('div', class_='list-blog-name').text.strip()
                body = div.find('div', class_='list-blog-descr').text.strip()
                event_date_plus = div.find('div', class_='blog-event-item-date').text.split()
                event_date = event_date_plus[2].split('.')
                event_day = f'{event_date[2]}-{event_date[1]}-{event_date[0]} 21:00'
                format_date = '%Y-%m-%d %H:%M'
                event_dt = datetime.strptime(event_day, format_date)
                self.items.append({
                    "title": title,
                    "body": body,
                    'event_time': event_dt,
                    **PLACE_DIR
                })

            except Exception as e:
                logger.error('Something Wrong, error: %s', e)
