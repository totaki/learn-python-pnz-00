from django.core.management.base import BaseCommand
from scheduler.scheduler import Scheduler
from fetcher.fetcher import Fetcher
from typing import List

TASKS_MAP = {
    'fetcher': Fetcher()
}


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('tasks', type=List)
        parser.add_argument('timeout', type=int)

    def handle(self, *args, **options):
        tasks = TASKS_MAP[options['tasks']]
        timeout = options['timeout']
        scheduler = Scheduler(tasks, timeout)
        scheduler.run()
