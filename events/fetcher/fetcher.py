import requests
import logging
from parsers.base_parser import BaseParser
from typing import List


logger = logging.getLogger(__name__)


class Fetcher:

    def __init__(self, parsers: List[BaseParser]):
        self.parsers = parsers

    def __call__(self, *args, **kwargs) -> List:
        results = []
        for parser in self.parsers:
            method, url, params = parser.get_request_params()
            pars_func = getattr(requests, method)
            try:
                result = pars_func(url, **params)
                result.raise_for_status()
                parser.parse(result.text)
                results.extend(parser.items)
            except (requests.RequestException, requests.Timeout):
                logger.error(f'Ошибка ответа удаленного сервера')
        return results