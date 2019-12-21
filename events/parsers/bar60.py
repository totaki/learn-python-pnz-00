import logging
from bs4 import BeautifulSoup
from events.parsers.base_parser import BaseParser
from datetime import datetime


class BarParser(BaseParser):

    def get_request_params(self):  # -> Tuple[str, str, dict]:
        return 'get', 'http://bar60.ru/events', {
            'params': {
                'categoryId': '0',
                'date': datetime.now().strftime("%d.%m.%Y")
            }
        }

    def parse(self, html: str) -> None:
        """
        Это метод должен парсить страницу и добавлять найденные events в
        items
        """
        logger = logging.getLogger(__name__)
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
                logger.error('data')
            except Exception as e:
                logger.error('Something Wrong, error: %s', e)
