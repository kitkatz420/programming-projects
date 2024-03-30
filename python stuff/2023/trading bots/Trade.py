import MetaTrader5 as mt5

class Trade:
    def __init__(self):
        mt5.initialize() # Initialize MT5 connection

    def open_trade(self, lot_size, stop_loss, take_profit, trade_type, symbol):
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot_size,
            "type": trade_type,
            "sl": stop_loss,
            "tp": take_profit,
            "magic": 12345 # Magic number for identifying trades
        }

        result = mt5.order_send(request)
        return result

    def modify_trade(self, ticket, stop_loss, take_profit):
        request = {
            "action": mt5.TRADE_ACTION_SLTP,
            "ticket": ticket,
            "sl": stop_loss,
            "tp": take_profit,
        }

        result = mt5.order_send(request)
        return result
    
    def close_trade(self, ticket):
        result = mt5.Close(symbol, ticket=ticket)
        return result

    

    def __del__(self):
        mt5.shutdown() # Shutdown MT5 connection when the Trade object is destroyed
   
def test_trade_class():
    trade = Trade()

    # Test opening a trade
    lot_size = 0.1
    stop_loss = 50
    take_profit = 100
    trade_type = "BUY" # Use mt5.ORDER_SELL for sell trade
    symbol = "EURUSD"
    trade_ticket = trade.open_trade(lot_size, stop_loss, take_profit, trade_type, symbol)
    print("Trade opened with ticket:", trade_ticket)

    # Test modifying the trade
    new_stop_loss = 60
    new_take_profit = 120
    modify_result = trade.modify_trade(trade_ticket, new_stop_loss, new_take_profit)
    print("Trade modified:", modify_result)

    # Test closing the trade
    close_result = mt5.Close("EURUSD")
    print("Trade closed:", close_result)

if __name__ == "__main__":
    test_trade_class()
