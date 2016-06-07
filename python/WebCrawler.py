from bs4 import BeautifulSoup

import requests


def trade_spider(max_pages):

        page = 1

        filSlutpris = open('slutpris.txt', 'w')
        filAdress = open('adress.txt', 'w')
        filSald = open('datum.txt', 'w')
        filM2pris = open('m2pris.txt', 'w')


        url = 'http://www.hemnet.se/salda/bostader?commit=&item_types%5B%5D=bostadsratt&living_area_min=45&location_ids%5B%5D=17744&page=' + str(page) + '&selling_price_max=4000000'
        source_code = requests.get(url)
        plain_text = source_code.text
        # print(plain_text)
        soup = BeautifulSoup(plain_text)
        for list in soup.findAll('ul', {'class': 'results sold clear-children'}):
                for item in list.findAll('div', {'class': 'item sold result normal'}):
                        #print(item)
                        #print('--------')
                        slutpris = item.findAll('li', {'class': 'price item-result-meta-attribute-is-bold'})[0].contents[1].string
                        slutpris2 = [int(s) for s in slutpris.split() if s.isdigit()]
                        adress = item.findAll('h2', {'class': 'hide-element section-label text--subtle'})[0].string
                        sald = item.findAll('li', {'class': 'sold-date black item-result-meta-attribute-is-bold'})[0].string
                        m2pris = item.findAll('li', {'class': 'price-per-m2'})[0].string
                        for x in range(0,10):
                                print(item.contents[x].string)
                                for y in range(0,10):
                                        #print(item.contents[5].contents[y])

                        #print('*****SLUTPRIS*******')
                        #print(slutpris)
                        #filSlutpris.write(slutpris + ',')
                        #print(',,,,,ADRESS,,,,,,,')
                        #print(adress)
                        #filAdress.write(adress + ',')
                        # print('.....SALD..........')
                                        print(sald.replace("\n", " ").strip())
                        #filSald.write(sald + ',\n')
                        # print(',,,,,KVADRATMETERPRIS,,,,,')
                        # print(m2pris)
                        #filM2pris.write(m2pris + ',')


        # print(soup)
        # soup1 = soup.prettify()
        # print(soup1)
        filSlutpris.close()
        filAdress.close()
        filM2pris.close()
        filSald.close()
trade_spider(1)


