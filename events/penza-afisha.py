import requests
from bs4 import BeautifulSoup
from datetime import datetime


def today_url():
    """today_url -> string"""
    url = 'http://penza-afisha.ru/index.php?date='
    today = datetime.now()
    return url + today.strftime("%Y%m%d")


def get_html(url):
    """
    получаем HTML страницы сайта
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    r = requests.get(url, headers=headers)
    if r.ok:  # 200 - True, another 403, 404 - False
        return r.text
    else:
        print(r.status_code)


def get_films_url(html):
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.find('div', class_="col2").find_all('div')
    films_urls = []
    for div in divs:
        """_________ФИЛЬМЫ___________"""
        try:
            trs = div.find('table', id="tab_films").find_all('tr')
            for td in trs:
                items = td.find_all('a')
                for item in items:
                    url = 'http://penza-afisha.ru/' + item.get('href') + '\n'
                    if 'http://penza-afisha.ru/films.php?' in url:
                        films_urls.append(url)

            return list(set(films_urls))

        except:
            return 'NO DATA'


def get_other_events_url(html):
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.find('div', class_="col2").find_all('div', class_="text_col1")[2]
    events = []
    for div in divs:
        try:
            trs = div.find_all('tr')
            for td in trs:
                items = td.find_all('a')
                for item in items:
                    url = 'http://penza-afisha.ru/' + item.get('href') + '\n'
                    if 'orgs' in url:
                        continue
                    events.append(url)

            return list(set(events))

        except:
            return 'NO DATA'


def film_season_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find_all('tr')
    seasons = []
    i = 6
    for td in trs:
        try:
            season = trs[i].text.strip().replace('\n', ' ')
            if 'руб' not in season:
                break
            # print(season)
            seasons.append(season)
            i += 2
        except:
            break

    return seasons


def get_film_info(html, url):
    seasons_html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    title = soup.find('div', class_='lc_fulf').find('div', class_='header_row').text
    table = soup.find('div', class_='lc_fulf').find('div', class_='text_col1')
    trs = table.find_all('td')
    production = trs[3].text
    creation_year = trs[5].text.strip()
    genre = trs[9].text.strip()
    role = trs[13].text.strip()
    description = trs[19].text.strip()

    data = {
        'Название': title,
        'Производство': production,
        'Год создания': creation_year,
        'Жанр': genre,
        'В ролях': role,
        'Описание': description,
        'Расписание': film_season_data(seasons_html)
    }

    return data


def get_events_info(html):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.find('div', class_='lc_fulf').find('div', class_='header_row').text
    divs = soup.find('div', class_='lc_fulf').find('div', class_='text_col1').find_all('td')

    try:
        info = divs[1].text.split()[:-5]
        info = ' '.join(info)
    except:
        info = 'No information'

    try:
        description = divs[14].text
    except:
        description = 'No information'

    data = {
        'Название': title,
        'Информация': info,
        'Описание': description
    }

    return data


def main():
    html = get_html(today_url())
    urls = get_films_url(html) + get_other_events_url(html)
    all_events_data = []
    for url in urls:
        if 'films' in url:
            film_html = get_html(url)
            seasons_url = url.replace('films', 'seans').replace('?f', '?film')
            # 'http://penza-afisha.ru/seans.php?film=3722'
            film_data = get_film_info(film_html, seasons_url)
            all_events_data.append(film_data)

        else:
            event_html = get_html(url)
            event_data = get_events_info(event_html)
            all_events_data.append(event_data)

    return all_events_data


if __name__ == '__main__':
    for events in main():
        print(events)
