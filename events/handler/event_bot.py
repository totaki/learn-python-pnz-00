import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler
from handler.models import User, Tag, Notificaton
from telegram import ReplyKeyboardMarkup

logger = logging.getLogger(__name__)


def start(update):
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


def tags(update):
    """Print tags"""
    user_id = update.message.chat.id
    db_id = User.objects.get(external_id=user_id)
    if user_id in db_id:
        concert_tags = ['Rock', 'Pop', 'Game', 'Classic']
        tag_keyboard = ReplyKeyboardMarkup([concert_tags])
        update.message.reply_text('Choose tag', reply_markup=tag_keyboard)
    else:
        update.message.reply_text('Use command: /start, to start working with bot')


def create_notifications(update, user_data):
    """Create notification in database"""
    chat_id = update.message.chat.id
    Notification.objects.create(tag=user_data[0], chat_id=chat_id)
    update.message.reply_text(f'You are subscribed to {user_data}')


def send_notifications(chat_id, message):
    pass


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def event_bot(token, PROXY):
    """Start the bot."""
    updater = Updater(token, request_kwargs=PROXY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("tags", tags))
    dp.add_handler(
        RegexHandler('^()$',
                     send_cat,
                     pass_user_data=True)
    )
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()
