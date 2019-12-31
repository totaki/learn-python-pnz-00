import logging
from django.core.management.base import BaseCommand
from handler.event_bot import event_bot
from events.settings import PROXY

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('token', type=str)

    def handle(self, *args, **options):
        token = options['token']
        if token:
            event_bot(token, PROXY)
        else:
            logger.error('Ошибка получения токена')