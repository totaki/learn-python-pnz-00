from datetime import datetime, timedelta


class Task:
    def __init__(self, timeout, runner, callback):
        self.timeout = timeout  # в секундах
        self.runner = runner  # Сама функция, которая будет запускаться, в нашем случае Fetcher
        self.callback = callback  # Сюда мы будем передавать результат, сохранить ивенты
        self.next = datetime.utcnow()

    @property
    def need_run(self, datetime):
        """
        тут надо реализовать проверку того что мы должны запустить данные таск,
        в нашем случае просто проверяем что self.next меньше времени, которое мы передали
        """
        return self.next < datetime

    def update_next(self):
        """
        Тут обновляем наш next
        """
        self.next = self.next + timedelta(seconds=self.timeout)


