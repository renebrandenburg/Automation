import bs4, requests
import sys

if len(sys.argv) < 2:
    print('Give name of game as argument')
    sys.exit(0)


search_term = sys.argv[1]

def getBolPrices(product):
    product_url = f'https://www.bol.com/nl/s/?searchtext={product}&searchContext=media_all&appliedSearchContextId=&suggestFragment={product}&adjustedSection=&originalSection=main&originalSearchContext=media_all&section=main&N=0&defaultSearchContext=media_all'
    res = requests.get(product_url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('.product-item--row')
    # TODO Fix display
    prices = []
    for elem in elems:
        name = elem.select('.product-title')[0].text.strip()
        price = elem.select('.price-block')[0].select('meta')[0].attrs['content'].strip()
        prices.append(f'{name}: {price}')
    return prices


prices = getBolPrices(search_term)

print('The price is ' + '\n'.join(prices))