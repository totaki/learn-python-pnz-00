from django.core.management.base import BaseCommand
from fetcher.fetcher import Fetcher
from parsers.rostokhall_parser import RostokhallParser
from parsers.bar60 import BarParser
from scheduler.notification_callback import get_notification_runner
from scheduler.save_event import save_event
from scheduler.task import Task
from scheduler.scheduler import Scheduler
from scheduler.check_event import check_event
from events.settings import PROXY


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('token', type=str)
        parser.add_argument('timeout', type=int)

    def handle(self, *args, **options):
        token = options['token']
        tasks = [
            Task(1000, Fetcher([RostokhallParser, BarParser]), save_event),
            Task(1000, check_event, get_notification_runner(token, PROXY))
        ]
        scheduler = Scheduler(tasks, options['timeout'])
        scheduler.run()
