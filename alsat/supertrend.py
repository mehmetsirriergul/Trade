from binance.client import Client
import talib as ta
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import sys
import math
import ayarlar 


client=Client(ayarlar.api_key,ayarlar.secret_key)


def generateSupertrend(close_array, high_array, low_array, atr_period, atr_multiplier):

    try:
        atr = ta.ATR(high_array, low_array, close_array, atr_period)
    except:
        print('exception in atr:', sys.exc_info()[0], flush=True)
        
        return False, False

    previous_final_upperband = 0
    previous_final_lowerband = 0
    final_upperband = 0
    final_lowerband = 0
    previous_close = 0
    previous_supertrend = 0
    supertrend = []
    supertrendc = 0

    for i in range(0, len(close_array)):
        if np.isnan(close_array[i]):
            pass
        else:
            highc = high_array[i]
            lowc = low_array[i]
            atrc = atr[i]
            closec = close_array[i]

            if math.isnan(atrc):
                atrc = 0

            basic_upperband = (highc + lowc) / 2 + atr_multiplier * atrc
            basic_lowerband = (highc + lowc) / 2 - atr_multiplier * atrc

            if basic_upperband < previous_final_upperband or previous_close > previous_final_upperband:
                final_upperband = basic_upperband
            else:
                final_upperband = previous_final_upperband

            if basic_lowerband > previous_final_lowerband or previous_close < previous_final_lowerband:
                final_lowerband = basic_lowerband
            else:
                final_lowerband = previous_final_lowerband

            if previous_supertrend == previous_final_upperband and closec <= final_upperband:
                supertrendc = final_upperband
            else:
                if previous_supertrend == previous_final_upperband and closec >= final_upperband:
                    supertrendc = final_lowerband
                else:
                    if previous_supertrend == previous_final_lowerband and closec >= final_lowerband:
                        supertrendc = final_lowerband
                    elif previous_supertrend == previous_final_lowerband and closec <= final_lowerband:
                        supertrendc = final_upperband

            supertrend.append(supertrendc)

            previous_close = closec

            previous_final_upperband = final_upperband

            previous_final_lowerband = final_lowerband

            previous_supertrend = supertrendc

    return supertrend
