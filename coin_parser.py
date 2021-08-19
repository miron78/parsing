import requests
from bs4 import BeautifulSoup

URL = 'https://ru.ucoin.net/catalog'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
    'accept': '*/*'
}
HOST = 'https://ru.ucoin.net'

def get_data():
    r = requests.get(url=URL, headers=HEADERS)
    soup = BeautifulSoup(r.text, 'lxml')
    items = soup.find_all('li', class_='cntry')

    country = []
    for item in items:
        country.append(item.find('a').get('href').split('=')[1])

    country_period = []
    for i in country:
        url = URL + f'/?country={i}'

        r = requests.get(url=url, headers=HEADERS)
        soup = BeautifulSoup(r.text, 'lxml')

        page_count = int(soup.find('div', class_='pages').find_all('a')[-1].text)

        for page




def main():
    get_data()

if __name__ == '__main__':
    main()
