import sqlite3
import logging
from sqlite3 import Error
from typing import List

logging.basicConfig(filename="to_saved_into_db.log", level=logging.INFO)


def db_connect():
    try:
        db = sqlite3.connect('db.sqlite3')
        return db
    except Error:
        logging.error('Error connect database')


def save_events(db, events: List) -> List[id]:
    cursor = db.cursor()
    cursor.execute('SELECT title FROM events')
    rows = cursor.fetchall()
    for row in rows:
        for event in events:
            if row != event['title']:
                event_list = event.values()
                cursor.execute('INSERT INTO events(title, body, event_time, place_name, city, street, house_number) '
                               'VALUES(?, ?, ?, ?, ?, ?, ? )', event_list)
            else:
                cursor.execute('SELECT event_time FROM events WHERE title = row')
                rows_event_time = cursor.fetchall()
                if rows_event_time[0] != event['event_time']:
                    cursor.execute(
                        'INSERT INTO events(title, body, event_time, place_name, city, street, house_number) '
                        'VALUES(?, ?, ?, ?, ?, ?, ? )', event_list)
                else:
                    logging.info(f'Событие {row} уже есть в базе')
                    break
    return [111, 222] #возврат id пока не реализовал





