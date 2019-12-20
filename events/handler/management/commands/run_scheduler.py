from django.core.management.base import BaseCommand, CommandError
from events.scheduler.Scheduler import Scheduler


class Command(BaseCommand):
    """
    Command run scheduler
    """
    help = 'Run scheduler'

    def add_arguments(self, parser):
        parser.add_argument('tasks', type=list, help='Задачи на исполнение')
        parser.add_argument('timeout', type=int, help='Время ожидания', )

    def handle(self, *args, **options):
        tasks = options['tasks']
        timeout = options['timeout']

        scheduler = Scheduler(tasks, timeout)
        scheduler.run()
