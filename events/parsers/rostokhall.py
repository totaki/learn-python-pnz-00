from bs4 import BeautifulSoup


def get_events(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        all_events = soup.findAll('section', class_='AfishaEvent')

        rostokhall_events = []
        PLACE_DIR = {
            "place_name": 'Rostokhall',
            "city": "Penza",
            "street": "Zlobina",
            "house_number": "19"
        }
        for event in all_events:
            try:
                title = event.find('h0').text

                body = event.div.find(class_="AfishaEventText").text
                event_body = body.partition(title)
                event_body = event_body[2].strip()

                event_time = event.find('div', class_="AfishaEventData").text
                event_time = ' '.join(event_time.split())

                rostokhall_events.append({
                    "title": title,
                    "body": event_body,
                    "event_time": event_time,
                    **PLACE_DIR
                })
            except AttributeError:
                return f'Ошибка поиска по странице HTML'

        print(rostokhall_events)
        return rostokhall_events
    except TypeError:
        return f'Файл не обнаружен'


def open_html():
    try:
        with open("rostokhall1.html") as f:
            html = f.read()
            return html
    except FileNotFoundError:
        return False


if __name__ == "__main__":
    print(get_events(open_html()))
