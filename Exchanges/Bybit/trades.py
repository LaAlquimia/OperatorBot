from pybit.unified_trading import HTTP


session = HTTP()

session.place_order(
    category="linear",
    symbol="BTCUSDT",
    side="Buy",
    orderType="Market",
    reduceOnly=True,
    qty=0.001 )