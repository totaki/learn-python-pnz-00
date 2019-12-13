import requests
from bs4 import BeautifulSoup
from datetime import datetime


def today_url():
    """today_url -> string"""
    url = 'http://bar60.ru/events?categoryId=0&date='
    today = datetime.now()
    return url + today.strftime("%d.%m.%Y")


def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    else:
        return r.status_code


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.find_all('div', class_='blog-event')
    data = []
    for div in divs:
        try:
            title = div.find('div', class_='list-blog-name').text
            data.append(title)
            body = div.find('div', class_='list-blog-descr').text
            data.append(body)

        except:
            return 'NO DATA'

    return data


def main():
    url = today_url()
    html = get_html(url)
    get_data(html)


if __name__ == '__main__':
    main()
