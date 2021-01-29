import urllib.request
import json
from time import sleep
def get_coin_data(coins):
    url="https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR"
    r=urllib.request.urlopen(url)
    html=r.read()
    html=html.decode()
    d=json.loads(html)
    return d

# while True:
print(get_coin_data("BTC"))
sleep(5)
