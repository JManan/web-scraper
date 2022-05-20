import csv
from bs4 import BeautifulSoup
import requests

source = requests.get('https://coinmarketcap.com/').text

soup = BeautifulSoup(source, 'lxml')

all_crypto = soup.find('div', class_='h7vnx2-1 bFzXgL')

table = all_crypto.table
# print(table.prettify())

csv_file = open('scrape_file.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Sno', 'Name', 'Price', '24h %',
                    '7Days %', 'Market Cap', 'Volume', 'Circulating Supply'])

towrite = []
for row in table.tbody.select('tr')[:10]:
    for col in row:
        if (col.text != ''):
            towrite.append(col.text)
    csv_writer.writerow(towrite)
    towrite = []
csv_file.close()