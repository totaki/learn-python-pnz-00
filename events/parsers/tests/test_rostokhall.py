from events.parsers.rostokhall import open_html, get_events
import pytest


def test_open_html():
    """Результатом функции должна быть строка с содержимым файла rostokhall.html"""
    html = open_html()
    assert isinstance(html, str)


def test_get_events():
    """Результатом работы функции должен быть список словарей вида:
    [{
        "title": title,
        "body": event_body,
        "event_time": event_time,
        "place_name": 'Rostokhall',
        "city": "Penza",
        "street": "Zlobina",
        "house_number": "19"
    },
    {...},
    {...}
    ]"""
    event_list = get_events(open_html())
    assert isinstance(event_list, list)
