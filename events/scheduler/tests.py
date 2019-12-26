from django.test import TestCase
from scheduler.task import Task
from fetcher.fetcher import Fetcher
from scheduler.save_event import save_event
from parsers.bar60 import BarParser
from parsers.rostokhall_parser import RostokhallParser
from datetime import datetime

PARSER_MAP = {
    'parsers': [RostokhallParser(), BarParser()]
}


class BaseTaskTest(TestCase):
    def setUp(self):
        self.task = Task(30, Fetcher(PARSER_MAP['parsers']), save_event)
        self.datetime = datetime.utcnow()

    def test_need_run(self):
        """Тест проверки работы функции need_run, если текущее время больше записанного
        в self.task.next - возвращается True"""

        self.assertEqual(self.task.need_run(self.datetime), True)

    def test_update_next(self):
        """Тест проверки работы функции update_next, всё верно, если в результате значение,
        self.task.next увеличивается на self.timedelta"""

        seconds = 0
        self.task.next = datetime.strptime(
            f'2019-12-25 12:20:{seconds}', '%Y-%m-%d %H:%M:%S'
        )
        self.task.update_next()
        plus_delta = self.task.next
        result = datetime.strptime(
            f'2019-12-25 12:20:{seconds + self.task.timeout}', '%Y-%m-%d %H:%M:%S'
        )
        self.assertEqual(plus_delta, result)
