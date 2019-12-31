import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram.utils.request import Request
from django.core.paginator import Paginator

from handler.models import User, Tag, Notification, Event
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Bot

logger = logging.getLogger(__name__)

TAG_PREFIX = 'tag'
TAG_PAGINATOR_PREFIX = 'tag_paginator'


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


def tags(update, context):
    """Print tags"""
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    reply_markup = get_tags()
    update.message.reply_text(
        'Start handler, Choose a route',
        reply_markup=reply_markup
    )


def get_tags(current_page=1):
    concert_tags = Tag.objects.all()
    paginator = Paginator(concert_tags, 3)
    pagination_keyboard = []
    keyboard = []
    page = paginator.page(current_page)
    for tag in page.object_list:
        keyboard.append([(InlineKeyboardButton(
            str(tag.title),
            callback_data=f'{TAG_PREFIX}:{tag.id}'
        ))])
    if page.has_previous():
        pagination_keyboard.append(InlineKeyboardButton(
            '<< Previous',
            callback_data=f'{TAG_PAGINATOR_PREFIX}:{page.previous_page_number()}'
        ))
    if page.has_next():
        pagination_keyboard.append(InlineKeyboardButton(
            'Next >>',
            callback_data=f'{TAG_PAGINATOR_PREFIX}:{page.next_page_number()}'
        ))
    keyboard.append(pagination_keyboard)
    return InlineKeyboardMarkup(keyboard)


def create_notifications(update, context):
    """Create notification in database"""
    chat_id = update.effective_chat.id
    query = update.callback_query
    prefix, answer = query.data.split(':')
    reply_markup = None
    message = 'Callback data incorrect'
    if prefix == TAG_PREFIX:
        tag = Tag.objects.get(id=answer)
        user = User.objects.get(external_id=chat_id)
        user.tags.add(tag)
        message = f'You are subscribed to {tag.title}'
    elif prefix == TAG_PAGINATOR_PREFIX:
        reply_markup = get_tags(answer)
        message = update.effective_message.text
    update.callback_query.edit_message_text(text=message, reply_markup=reply_markup)


def get_event_notificator(token, request_kwargs):
    request = Request(**request_kwargs)
    bot = Bot(token, request=request)

    def send(user, event):
        name_event = event.title
        date_event = event.event_time
        chat = user.external_id
        text = f'{name_event} выступает {date_event}'
        bot.send_message(chat, text)
    return send


def send_notifications(update, context, chat_id, event):
    context.bot.send_message(chat_id=chat_id, text=f'Новое событие по вашей подписке:'
                                                   f'{event.title}, {event.body}')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def event_bot(token, PROXY):
    """Start the bot."""
    updater = Updater(token, request_kwargs=PROXY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("tags", tags))
    dp.add_handler(CallbackQueryHandler(create_notifications))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()
