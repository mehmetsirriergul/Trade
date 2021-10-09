import ayarlar
import csv
from binance.client import Client

client = Client(ayarlar.API_KEY, ayarlar.API_SECRET)

candles = client.get_account()
print(candles)

'''csvfile=open('2012-2020.csv', 'w', newline='')

candlestick_writer=csv.writer(csvfile, delimiter=',')

candlesticks =client.get_historical_klines("BTCUSDT",Client.KLINE_INTERVAL_5MINUTE,"1 Jan,2020","30 May,2021")
       
for candlestick in candlesticks:
    candlestick_writer.writerow(candlestick)
csvfile.close() '''