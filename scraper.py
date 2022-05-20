import csv
from bs4 import BeautifulSoup
import requests

source = requests.get('https://coinmarketcap.com/').text

soup = BeautifulSoup(source, 'lxml')

all_crypto = soup.find('div', class_='h7vnx2-1 bFzXgL')

table = all_crypto.table
# print(table.prettify())

csv_file = open('scrape_file', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Sno', 'Name', 'Price', '24h %',
                    '7Days %', 'Market Cap', 'Volume'])

for row in table.tbody:
    # print(row.prettify())
    try:
        sno = row.find('p', class_='sc-1eb5slv-0 etpvrL').text
        print(sno)
        price = row.find('div', class_='sc-131di3y-0 cLgOOr').span.text
        print(price)
        name = row.div.div.div.p.text
        print(name)
        change1 = row.find('span', class_='sc-15yy2pl-0 kAXKAX').text
        print(change1)
        change2 = row.find('span', class_='sc-15yy2pl-0 hzgCfk').text
        print(change2)
        marketcap = row.find('p', class_='sc-1eb5slv-0 hykWbK').span.text
        print(marketcap)
        Volume = row.find(
            'div', class_='sc-16r8icm-0 j3nwcd-0 cRcnjD').a.p.text
        print(Volume)
        print()
    except Exception as e:
        print("Not Found")

    print()

    csv_writer.writerow([sno, name, price, change1,
                        change2, marketcap, Volume])

csv_file.close()
