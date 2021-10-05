import alsat.ayarlar as mse
from binance.client import Client
from django.shortcuts import render,HttpResponse
import datetime
import pandas as pd


client=Client(mse.api_key,mse.secret_key,tld='com')


def login(request):
    return render(request, 'binance/login.html')



def cuzdan(request):
    
    info=client.get_account()
    list=info['balances']
    exchange_info=client.get_exchange_info()
    symbols=exchange_info['symbols']
    print(symbols)
    
    return render(request, 'binance/cuzdan.html', {'list':list, 'symbols':symbols})
    

def anasayfa(request):

    return render(request, 'binance/anasayfa.html')

def index(request):
    
    return render(request, 'binance/index.html')

def buy(request):

    return render(request, 'binance/buy.html')

def sell(request):

    return render(request, 'binance/sell.html')

def settings(request):

    return render(request, 'binance/settings.html')

def base(request):

    return render(request, 'binance/base.html')

def userindex(request):

    return render(request, 'binance/userindex.html')


def apiindex(request):
    

    return render(request, 'binance/apiindex.html')




