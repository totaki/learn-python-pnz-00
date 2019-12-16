from abc import ABC, abstractmethod


class BaseParser(ABC):

    def __init__(self, requests_method, url, **kwargs):
        self.requests_method = requests_method
        self.url = url
        self.kwargs = kwargs
        self.items = []

    @abstractmethod
    def get_request_params(self):  # -> Tuple[str, str, dict]:
        """
        Это метод должен возвращать кортеж следующих данных
        - имя метода requests (get, post)
        - url
        - kwargs, которые будут добавлены в параметры запроса
        """
        params = (self.requests_method, self.url, self.kwargs)
        return params

    @abstractmethod
    def parse(self, string: str) -> None:
        """
        Это метод должен парсить страницу и добавлять найденные events в
        items
        """
        pass
