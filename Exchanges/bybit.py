
from pybit.unified_trading import WebSocket 
from time import sleep
import  os 




pdist = {
    
}


ws = WebSocket(
    testnet=False,
    channel_type="linear",
)

def handle_trade(message):
    global pdist     
    os.system("clear")
    info = message["data"][0]
    print('Side ','last_price ', 'Vol'  )
    print(info["S"], info["p"] , info["v"]   )

ws.trade_stream("TRBUSDT", handle_trade)


while True:
    sleep(0.1)
    