import bs4
import requests



def getBolPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('.promo-price')
    # TODO Fix display
    return elems[0].text.strip()


price = getBolPrice('https://www.bol.com/nl/p/the-last-of-us-part-ii-ps4/9200000072535107/?bltgh=m5Qn41dBogHUr81F2xFKNw.1_4.5.ProductTitle')

print('The price is ' + price)