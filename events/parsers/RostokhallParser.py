import requests
import logging
from bs4 import BeautifulSoup
from events.parsers.BaseParser import BaseParser

url = "https://rostokhall.ru/afisha/"
logging.basicConfig(filename="rostokhall.log", level=logging.INFO)


def get_html(url: str) -> str:
    """
    Метод получает html страницу используя библиотеку requests
    """
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except requests.RequestException:
        logging.error('Ошибка ответа удаленного сервера')


class RostokhallParser(BaseParser):

    def get_request_params(self):  # -> Tuple[str, str, dict]:
        """
        Это метод должен возвращать кортеж следующих данных
        - имя метода requests (get, post)
        - url
        - kwargs, которые будут добавлены в параметры запроса
        """
        pass

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
                    event_time = ' '.join(event_time.split())

                    self.items.append({
                        "title": title,
                        "body": event_body,
                        "event_time": event_time,
                        **PLACE_DIR
                    })
                except AttributeError:
                    logging.error('AttributeError - Ошибка поиска по странице HTML, отсутствует тег для поиска')
        else:
            logging.error('Ошибка, нет тэга "section, class_=AfishaEvent"')


a = RostokhallParser()
a.parse(get_html(url))
print(a.items)
