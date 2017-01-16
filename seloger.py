import requests, time
import pandas as pd
import numpy as np
from lxml import html
from pprint import pprint
from crawlers_beta import SeLogerCrawler
from collections import OrderedDict

def formatting(item):

    # loading features
    features = OrderedDict()
    features['Price'] = item['price']
    features['Surface'] = item['surface']
    features['Furnished'] = item['furnitures']
    features['Lift'] = item['lift']
    features['Nb_rooms'] = item['rooms']
    features['Paris_2'] = 0
    features['Paris_3'] = 0
    features['Paris_4'] = 0
    features['Paris_5'] = 0
    features['Paris_6'] = 0
    features['Paris_7'] = 0
    features['Paris_8'] = 0
    features['Paris_9'] = 0
    features['Paris_10'] = 0
    features['Paris_11'] = 0
    features['Paris_12'] = 0
    features['Paris_13'] = 0
    features['Paris_14'] = 0
    features['Paris_15'] = 0
    features['Paris_16'] = 0
    features['Paris_17'] = 0
    features['Paris_18'] = 0
    features['Paris_19'] = 0
    features['Paris_20'] = 0
    features['Heating_collectif'] = 0
    features['Heating_individuel'] = 0
    features['Heating_src_electricite'] = int(item['energy']['electricite'])
    features['Heating_src_fuel'] = int(item['energy']['fuel'])
    features['Heating_src_gaz'] = int(item['energy']['gaz'])
    features['Gardien'] = item['gardien']
    features['Internet'] = item['internet']

    if item['heating'] == 'individuel':
        features['Heating_individuel'] = 1
    else:
        features['Heating_collectif'] = 1

    if item['area'] != 1:
        area_name = 'Paris_' + str(item['area'])
        features[area_name] = 1

    if not item['charges']:
        features['Charges'] = np.nan
    else:
        features['Charges'] = item['charges']

    return features


def get_urls():
    start_url = (
        'http://www.seloger.com/list.htm?tri=initial'
        '&idtypebien=1&idtt=1&cp=75&LISTING-LISTpg={}'
    )

    headers = {
        'Accept': (
            'text/html,application/xhtml+xml,'
            'application/xml;q=0.9,*/*;q=0.8'
        ),
        'Accept-Language': 'en',
        'User-Agent': (
            'Mozilla/5.0 (X11; Linux x86_64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/49.0.2623.110 Safari/537.36'
        )
    }

    url_list = []
    page_max = 5

    for page_id in range(1, page_max + 1):
        response = requests.get(start_url.format(page_id), headers=headers)
        tree = html.fromstring(response.text)
        urls = tree.xpath('//a[@class="listing_link slides"]/@href')
        url_list.extend(urls)
        time.sleep(0.1)
        print ('Scraping URLS page {0}/{1}. Urls collected : {2}'.format(
                page_id, page_max, len(url_list)))
    
    print ('Start scraping urls...')
    
    data = []

    for i, url in enumerate(url_list):
        try:
            print ('Crawling url {0}/{1}'.format(i, len(url_list)))
            crawler = SeLogerCrawler(url)
            row = formatting(crawler.__dict__)
            data.append(row)
        except:
            pass
    df = pd.DataFrame(data)
    df.to_csv('seloger_data.csv')

if __name__ == '__main__':
    get_urls()