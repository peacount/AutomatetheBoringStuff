# web scraping
import bs4
import requests
res = requests.get('https://www.amazon.de/-/en/Al-Sweigart/dp/1593279922/ref=sr_1_1?dchild=1&keywords=automate+the+boring+stuff&qid=1609163523&sr=8-1')
res.raise_for_status

soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('#buyNewSection > div > div > span > span')
elems[0].text.strip()

import bs4, requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#mediaNoAccordion > div.a-row > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')
    return elems[0].text.strip()

price = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-2nd-ebook/dp/B07VSXS4NK')
print('The price is ' + price)



