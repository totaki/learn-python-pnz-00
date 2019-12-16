from abc import ABC, abstractmethod


class BaseParser(ABC):
    name: str

    def __init__(self):
        self.items = []

    @abstractmethod
    def get_request_params(self):  # -> Tuple[str, str, dict]:
        """
        Это метод должен возвращать кортеж следующих данных
        - имя метода requests (get, post)
        - url
        - kwargs, которые будут добавлены в параметры запроса
        """
        pass

    @abstractmethod
    def parse(self, string: str) -> None:
        """
        Это метод должен парсить страницу и добавлять найденные events в
        items
        """
        pass
