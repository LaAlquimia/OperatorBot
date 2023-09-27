

import os, sys
from time import sleep
sys.path.append('././')
from api_keys import api_secret, api_key
from pybit.unified_trading import WebSocket, HTTP


ws = WebSocket(
    api_key = api_key,
    api_secret = api_secret,
    testnet=False,
    channel_type="private",
    
)

client = HTTP(
    api_key = api_key,
    api_secret = api_secret,
    testnet = False

) 


public_ws = WebSocket(
    testnet=False,
    channel_type="linear",
    
)

coin = "TRBUSDT"

pdist = {
}


def handle_trade(message):    
    global pdist
    info = message["data"]
    long = info[1]
    short = info[0]
    pdist[long['symbol']]= {
        'long': {            
            'entryPrice': long['entryPrice'],
            'size': long['size']
        },
        'short': {            
            'entryPrice': short['entryPrice'],
            'size': short['size']
        }
    }


def handle_info(message):
    global pdist     
    os.system("clear")
    info = message["data"][0]
    price = float(info["p"])
    print('Side ','last_price ', 'Vol'  )
    print(info["S"], price , info["v"])
    if pdist :        
        st = pdist[coin]['short']
        lg = pdist[coin]['long']
        long_entry = float(lg['entryPrice'])
        short_entry = float(st['entryPrice'])
        print(f'''
    short ent: {float(st['entryPrice'])}
        pdist: { [round(((short_entry-price)/short_entry)*100 , 4) if short_entry > 0 else short_entry]} %
    
    long ent: {float(lg['entryPrice'])} 
        pdist: {[round(((price -long_entry)/long_entry)*100 , 4) if long_entry > 0 else long_entry]} %
    
              ''' )

    
    




def handle_positions(message):
    return(0)

ws.position_stream(callback=handle_trade)
public_ws.trade_stream(symbol= coin, callback=handle_info)

while True:
    sleep(1)
    