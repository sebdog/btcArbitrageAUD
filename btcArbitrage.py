# S Lewandowski
# Jan 2018

import math
import requests
import json
import locale

from prettytable import PrettyTable

csURL = "https://www.coinspot.com.au/pubapi/latest/"
bmURL = "https://api.btcmarkets.net/market/BTC/AUD/tick"
acxURL = "https://acx.io/api/v2/tickers/"

csReq = requests.get(csURL)
csData = csReq.json()

bmReq = requests.get(bmURL)
bmData = bmReq.json()

acxReq = requests.get(acxURL)
acxData = acxReq.json()

#print(csData)
csBuy=csData['prices']['btc']['bid']
csSell=csData['prices']['btc']['ask']


#print(bmData)
bmBuy=bmData['bestBid']
bmSell=bmData['bestAsk']


#print(acxData)
acxBuy=acxData['btcaud']['ticker']['buy']
acxSell=acxData['btcaud']['ticker']['sell']

t = PrettyTable(['Exchange','Buy','Sell'])
t.add_row(['BTC Markets',bmBuy,bmSell])
t.add_row(['CoinSpot',csBuy,csSell])
t.add_row(['ACX',acxBuy,acxSell])

print(t)
