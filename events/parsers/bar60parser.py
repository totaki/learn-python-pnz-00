import logging
from bs4 import BeautifulSoup
from events.parsers.BaseParser import BaseParser
from datetime import datetime

logging.basicConfig(filename="bar60parser.log", level=logging.INFO)


class BarParser(BaseParser):

    def get_request_params(self):  # -> Tuple[str, str, dict]:
        return 'GET', 'http://bar60.ru/events?q=query', {}

    def parse(self, html: str) -> None:
        """
        Это метод должен парсить страницу и добавлять найденные events в
        items
        """

        soup = BeautifulSoup(html, 'lxml')
        divs = soup.find_all('div', class_='blog-event')
        for div in divs:
            try:
                title = div.find('div', class_='list-blog-name').text
                body = div.find('div', class_='list-blog-descr').text

                self.items.append({
                    "title": title,
                    "body": body,
                    'place': 'Bar60',
                    'time': datetime.now().strftime("%d.%m.%Y"),
                    'city': 'Penza',
                    'street': 'Moskovskaya 60'
                })

            except:
                logging.error('No data')