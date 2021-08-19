import json

from bs4 import BeautifulSoup
import csv

with open("index.html", encoding="utf-8") as file:
    src = file.read()

with open('period.csv', 'w') as file:
    writer = csv.writer(file)

    writer.writerow(
        (
            'Country',
            'Period_ID'
        )
    )

soup = BeautifulSoup(src, 'lxml')
country_all = soup.find_all('a', class_='period')

countrys = []
for country in country_all:

    try:
        name = country.get('href').split('=')[1].split('&')[0]
    except:
        name = 'no country'

    try:
        period_id = country.get('pid')
    except:
        period_id = 'no period_id'

#     print(name)
#     print(period_id)
#     print("*" * 10)
#
    countrys.append(
        {
            'name': name,
            'period_id': period_id
        }
    )

    with open('period.csv', 'a') as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                name,
                period_id
            )
        )
with open('period.json', 'w') as file:
    json.dump(countrys, file, indent=4, ensure_ascii=False)

print(countrys)