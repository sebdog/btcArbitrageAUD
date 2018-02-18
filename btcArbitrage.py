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
csBuy=float(csBuy)
csSell=float(csSell)

#print(bmData)
bmBuy=bmData['bestBid']
bmSell=bmData['bestAsk']

#print(acxData)
acxBuy=acxData['btcaud']['ticker']['buy']
acxSell=acxData['btcaud']['ticker']['sell']
acxBuy=float(acxBuy)
acxSell=float(acxSell)

t = PrettyTable(['Exchange','Buy','Sell'])
t.add_row(['BTC Markets',bmBuy,bmSell])
t.add_row(['CoinSpot',csBuy,csSell])
t.add_row(['ACX',acxBuy,acxSell])

print(t)

csFee =0.01	#1%
bmFee =0.0085	#0.85%
acxFee=0.002	#0.2%


buy=[csBuy,bmBuy,acxBuy]
sell=[csSell,bmSell,acxSell]
exchange=['CoinSpot','BTC Markets','ACX']

for x in range(0,3):
	for y in range(0,3):
		if x != y:
			if buy[x]>sell[y]:
				print 'Buy '+exchange[y]
				print 'Sell '+exchange[x]+'\n'
			
