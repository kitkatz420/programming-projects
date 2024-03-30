import MetaTrader5 as mt5

class Trade:
    magic_number = 12345
    
    def __init__(self):
        mt5.initialize() # Initialize MT5 connection
    
    
    def get_info(symbol):
        
        info = mt5.symbol_info(symbol)
        
        return info
    
    def open_trade(self, symbol, action, lot, sl, tp, deviation):
        
        
        #symbol_Info = Trade.get_info(symbol)
        
        if action == 'buy':
            trade_type = mt5.ORDER_TYPE_BUY
            price = mt5.TICK_FLAG_ASK
            
        elif action == 'sell':
            trade_type = mt5.ORDER_TYPE_SELL
            price = mt5.TICK_FLAG_BID
        
        
        #point = symbol_Info.point
        
        buy_request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": trade_type,
            "price": price,
            "sl": sl,
            "tp": tp,
            "magic": Trade.magic_number, # Magic number for identifying trades
            "comment": "sent by python",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_RETURN
        }

        result = mt5.order_send(buy_request)
        return result

    def modify_trade(self, ticket, sl, tp):
        request = {
            "action": mt5.TRADE_ACTION_SLTP,
            "ticket": ticket,
            "sl": sl,
            "tp": tp,
        }

        result = mt5.order_send(request)
        return result
    
    def close_trade(self, action, buy_request, result, deviation):
        symbol = buy_request['symbol']
        lot = buy_request['volume']
        position_id = result.order
        if action == 'buy':
            trade_type = mt5.ORDER_TYPE_BUY
            price = mt5.TICK_FLAG_ASK
            
        elif action == 'sell':
            trade_type = mt5.ORDER_TYPE_SELL
            price = mt5.TICK_FLAG_BID
        
        close_request = {
            "action": action,
            "symbol": symbol,
            "volume": lot,
            "type": trade_type,
            "position": position_id,
            "price": price,
            "deviation": deviation,
            "magic": Trade.magic_number,
            "comment": "python script close",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_RETURN
            
            }
        
        
        result = mt5.order_send(close_request)
        return result

    

    def __del__(self):
        mt5.shutdown() # Shutdown MT5 connection when the Trade object is destroyed
   
