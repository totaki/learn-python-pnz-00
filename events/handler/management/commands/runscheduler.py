from django.core.management.base import BaseCommand
from fetcher.fetcher import Fetcher
from parsers.rostokhall_parser import RostokhallParser
from parsers.bar60 import BarParser
from scheduler.save_event import save_event
from scheduler.task import Task
from scheduler.scheduler import Scheduler


TASK_MAP = {
    'tasks': [Task(10, Fetcher([RostokhallParser, BarParser]), save_event), ]
}


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('tasks', type=str)
        parser.add_argument('timeout', type=int)

    def handle(self, *args, **options):
        scheduler = Scheduler(TASK_MAP[options['tasks']], options['timeout'])
        scheduler.run()