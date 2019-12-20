import logging
from typing import Tuple
from bs4 import BeautifulSoup
from events.parsers.BaseParser import BaseParser
from datetime import date

logging.basicConfig(filename="rostokhall.log", level=logging.INFO)


class RostokhallParser(BaseParser):

    def get_request_params(self) -> Tuple[str, str, dict]:
        """
        Это метод должен возвращать кортеж следующих данных
        - имя метода requests (get, post)
        - url
        - kwargs, которые будут добавлены в параметры запроса
        """
        return ('get', "https://rostokhall.ru/afisha/", {})

    def parse(self, html: str) -> None:
        """
        Это метод должен парсить страницу и добавлять найденные events в
        items
        """

        PLACE_DIR = {
            "place_name": 'Rostokhall',
            "city": "Penza",
            "street": "Zlobina",
            "house_number": "19"
        }
        MONTH_REPLACE = {"января": "01", "февраля": "02", "марта": "03", "апреля": "04", "мая": "05",
                         "июня": "06", "июля": "07", "августа": "08", "сентября": "09", "октября": "10",
                         "ноября": "11", "декабря": "12"}
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
                    month = MONTH_REPLACE[month]
                    event_day = f'{today.year}-{month}-{event_time[0]} {event_time[2]}'
                    self.items.append({
                        "title": title,
                        "body": event_body,
                        "event_time": event_day,
                        **PLACE_DIR
                    })
                except AttributeError:
                    logging.error('AttributeError - Ошибка поиска по странице HTML, отсутствует тег для поиска')
        else:
            logging.error('Ошибка, нет тэга "section, class_=AfishaEvent"')
