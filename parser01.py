import requests
from bs4 import BeautifulSoup

URL = 'https://ru.ucoin.net/catalog'

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
    'accept': '*/*'
}

HOST = 'https://ru.ucoin.net'



def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('li', class_='cntry')

    country = []
    for item in items:
        country.append({
            'id': item.find('span', class_='right lgray-13').get_text(),
            'name_ru': item.find('span', class_='left wrap nopad').get_text(),
            'name_en': item.find('a').get('href').split('=')[1],
            'link': HOST + item.find('a').get('href'),
        })
    print(country)

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')

parse()