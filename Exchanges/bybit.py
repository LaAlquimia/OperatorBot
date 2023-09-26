
#%%

from pybit.unified_trading import WebSocket
from time import sleep
import  os 

ws = WebSocket(
    testnet=False,
    channel_type="linear",
)

def handle_message(message):
    os.system("clear")
    info = message["data"][0]
    print({
        "side":info["S"],
        "price":info["p"]
            }
        )

ws.trade_stream("TRBUSDT", handle_message)

while True:
    sleep(0.1)
    