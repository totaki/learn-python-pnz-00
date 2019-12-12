from bs4 import BeautifulSoup

def get_events(html):
    soup = BeautifulSoup(html, 'html.parser')
    all_events = soup.findAll('section', class_='AfishaEvent')
    rostokhall_events = []
    for event in all_events:
        title = event.find('h3').text

        body = event.div.find(class_="AfishaEventText").text
        event_body = body.partition(title)
        event_body = event_body[2].strip()

        event_time = event.find('div', class_="AfishaEventData").text
        event_time = ' '.join(event_time.split())

        rostokhall_events.append({
            "title": title,
            "body": event_body,
            "event_time": event_time,
            "place_name": 'Rostokhall',
            "city": "Penza",
            "street": "Zlobina",
            "house_number": "19"
        })
    print(rostokhall_events)

def open_html():
    with open("rostokhall.html") as f:
        html = f.read()
        return html

if __name__ == "__main__":
    get_events(open_html())
