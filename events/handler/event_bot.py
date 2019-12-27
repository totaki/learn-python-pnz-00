import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handler.models import User

logger = logging.getLogger(__name__)


def start(update, context):
    """Save user in database and send a message when the command /start is issued."""
    user_id = update.message.chat.id
    username = update.message.chat.username
    message_date = update.message.date
    try:
        User.objects.get(external_id=user_id)
        logger.error(f"The user {username} is in the database")
        update.message.reply_text('We already met.')
    except User.DoesNotExist:
        User.objects.create(external_id=user_id, name=username, creation_date=message_date)
        update.message.reply_text(f'Hi, {username}! Your id {user_id}. Now is {message_date}')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def event_bot(token, PROXY):
    """Start the bot."""
    updater = Updater(token, request_kwargs=PROXY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()
