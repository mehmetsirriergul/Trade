from binance.client import Client

from django.shortcuts import render



client=Client(api_key="pjp9hPunP3gz99AAjl90lP0txDG58m50IrdxEwGbPcGFFM1gQa2U4Rhsfl61SvZ1",api_secret="LZT8gOS4dsbyPDA4bn1APh5kXcLueMVQ2hYkY5MrSP2QK9QKtwgg0NGaA1hIoAj8",tld='com')


def login(request):
    return render(request, 'binance/login.html')



def cuzdan(request):
    info=client.get_account()
    print(info)
    return render(request, 'binance/cuzdan.html')
    

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




