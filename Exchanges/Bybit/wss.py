import os, sys
sys.path.append('././')
print(sys.path
      )
from api_keys import api_secret, api_key
from pybit.unified_trading import WebSocket

ws = WebSocket(
    api_key = api_key,
    api_secret = api_secret,
    testnet=False,
    channel_type="private",
    
)

def handle_trade(message):
    os.system("clear")
    info = message["data"]
    print({
        "Info":info,
        
            }
        )



def handle_positions(message):
    return(0)


ws.position_stream(callback=handle_trade)