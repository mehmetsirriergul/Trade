from binance.client import Client
import talib as ta
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from supertrend import generateSupertrend
import time
import ayarlar 

client=Client(ayarlar.api_key,ayarlar.secret_key)

def mum(symbol,interval,limit):
    while True:
        interval = interval

        pair = symbol

        limit = limit
            
        klines = client.get_klines(symbol=pair,interval=interval,limit=limit )
                
        open_time = [int(entry[0]) for entry in klines]
        open = [float(entry[1]) for entry in klines]
        high = [float(entry[2]) for entry in klines]
        low = [float(entry[3]) for entry in klines]
        close = [float(entry[4]) for entry in klines]
            

        close_array = np.asarray(close)
        high_array = np.asarray(high)
        low_array = np.asarray(low)

        new_time = [datetime.fromtimestamp(time / 1000) for time in open_time]

        new_time_x = [date.strftime("%y-%m-%d") for date in new_time]

        
        supertrend = generateSupertrend(close_array, high_array, low_array, atr_period=10, atr_multiplier=3)
  
        son_kapanis = close_array[-1]
        onceki_kapanis = close_array[-2]

        son_supertrend_deger = supertrend[-1]
        onceki_supertrend_deger = supertrend[-2]
        
        print("kapanış :",son_kapanis)
        print("önceki kapanış :",onceki_kapanis)
        print("strend :" ,son_supertrend_deger)
        print("önceki strend :" ,onceki_supertrend_deger)

        

        # renk yeşile dönüyor, trend yükselişe geçti
        if son_kapanis > son_supertrend_deger and onceki_kapanis < onceki_supertrend_deger:
            print('al sinyali')

        # renk kırmızıya dönüyor, trend düşüşe geçti
        if son_kapanis < son_supertrend_deger and onceki_kapanis > onceki_supertrend_deger:
            print('sat sinyali')
        
        time.sleep(20)

print(mum("ETHUSDT","1m",500))

