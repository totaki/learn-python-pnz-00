import logging
from typing import Tuple
from bs4 import BeautifulSoup
from parsers.base_parser import BaseParser
from datetime import date, datetime

logger = logging.getLogger(__name__)

PLACE_DIR = {
    "place_name": 'Rostokhall',
    "city": "Penza",
    "street": "Zlobina",
    "house_number": "19",
    "office_number": 0
}
MONTHS = [
    "января",
    "февраля",
    "марта",
    "апреля",
    "мая",
    "июня",
    "июля",
    "августа",
    "сентября",
    "октября",
    "ноября",
    "декабря"
]


MONTH_MAP = {
    month_name: '{:0>2}'.format(number)
    for number, month_name in enumerate(MONTHS, 1)
}


class RostokhallParser(BaseParser):

    def get_request_params(self) -> Tuple[str, str, dict]:
        """
        Это метод должен возвращать кортеж следующих данных
        - имя метода requests (get, post)
        - url
        - kwargs, которые будут добавлены в параметры запроса
        """
        return 'get', "https://rostokhall.ru/afisha/", {}

    def parse(self, html: str) -> None:
        """
        Это метод должен парсить страницу и добавлять найденные events в
        items
        """
        self.items = []
        soup = BeautifulSoup(html, 'html.parser')
        all_events = soup.findAll('section', class_='AfishaEvent')
        if all_events:
            for event in all_events:
                try:
                    title = event.find('h3').text
                    body = event.div.find(class_="AfishaEventText").text
                    event_body = body.partition(title)
                    event_body = event_body[2].strip()
                    event_time = event.find('div', class_="AfishaEventData").text
                    event_time = event_time.split()
                    today = date.today()
                    month = event_time[1].lower()
                    month = MONTH_MAP[month]
                    event_day = f'{today.year}-{month}-{event_time[0]} {event_time[2]}'
                    format_date = '%Y-%m-%d %H:%M'
                    event_day = datetime.strptime(event_day, format_date)
                    self.items.append({
                        "title": title,
                        "body": event_body,
                        "event_time": event_day,
                        **PLACE_DIR
                    })
                except AttributeError:
                    logger.error('AttributeError - Ошибка поиска по странице HTML, отсутствует тег для поиска')
        else:
            logger.error('Ошибка, нет тэга "section, class_=AfishaEvent"')
