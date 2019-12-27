from scheduler.task import Task
from datetime import datetime
from typing import List
from time import sleep


class Scheduler:

    def __init__(self, tasks: List[Task], timeout=1):
        self.tasks = tasks  # список задач
        self.timeout = timeout

    def run(self):
        """
        Данная функция в бесконечном цикле проходит по все задачам, проверяет пришло ли
        время их запускать методом need_run передавая туда текущее время,
        если да то   последовательно вызвает runner, полученный результат
        передает в callback и делает update_next. После того как пройдет по все задачам,
        засыпает на timeout
        """

        while True:
            for task in self.tasks:
                date = datetime.utcnow()
                if task.need_run(date):
                    result = task.runner()
                    task.callback(result)
                    task.update_next()
            sleep(self.timeout)
