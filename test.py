import requests
from bs4 import BeautifulSoup

URL = 'https://ru.ucoin.net/catalog/?country=austria'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
    'accept': '*/*'
}
HOST = 'https://ru.ucoin.net'

def get_data():
    r = requests.get(url=URL, headers=HEADERS)
    #
    # src = r.text
    # with open("index.html", "w", encoding="utf-8") as file:
    #     file.write(src)

    soup = BeautifulSoup(r.text, 'lxml')

    content = soup.find_all('div', class_='country')
    print(soup)

    #page_count = int(soup.find('div', class_='pages').find_all('a')[-1].text)

    # for i in range(2, 3):
    #     url = URL + f'&page={i}'
    #
    #     r = requests.get(url=url, headers=HEADERS)
    #     soup = BeautifulSoup(r.text, 'lxml')
    #
    #     items = soup.find('div', id='tree')
    #     print(items)

        #for i in items:
        #    country_nane = i.get('href').split('&')[0].split('=')[1]
        #    period = i.get('href').split('&')[1].split('=')[1]
        #    print(country_nane)
        #    print(period)

def main():
    get_data()

if __name__ == '__main__':
    main()
