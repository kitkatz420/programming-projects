import MetaTrader5 as mt5
import yfinance as yf
import datetime
import sys

class Trade:
    
    #symbol = "@YM"
    #timeFrame = mt5.TIMEFRAME_M1
    #symbol = "@YM"
    timeFrame = mt5.TIMEFRAME_M1
    #count = 5000
    #rates = mt5.copy_rates_from(symbol, timeFrame, datetime.datetime.now(), Trade.count)
        
    
    
    #closePrices = [candle[4] for candle in rates]
    # Strategy parameters
    shortMaPeriod = 10
    longMaPeriod = 20
    
    # Backtest the trading strategy
    totalTrades = 0
    winningTrades = 0
    losingTrades = 0
    profit = 0.0
    
    inPosition = False
    entryPrice = 0.0
    
    # def __init__(self):
    mt5.initialize()
      
    
    def __init__(self, symbol, timeFrame, count, rates):
        
        self.symbol = symbol
        self.timeFrame = timeFrame
        self.count = count
        self.rates = rates
        #mt5.initialize()    
        rates = mt5.copy_rates_from(symbol, timeFrame, datetime.datetime.now(), count)
       
    
        if mt5.initialize() != True:
            print("Inintialization failed!")
            mt5.shutdown()
            sys.exit()
            
        if rates is None:
            print("Failed to retrieve historical data.")
            mt5.shutdown()
            sys.exit()
    
    
    
class Sma(Trade):
# some values such as data, long_period and short_period may be moved if they are not used 
# more will have to be added to be sure
    #YM = Trade("@YM", Trade.timeFrame, 5000, mt5.copy_rates_from(Trade.symbol, Trade.timeFrame, datetime.datetime.now(), Trade.count))

     
    # def __init__(self):
    #     pass
    def calculate_ma(data, period):
        ma = sum(data[-period:]) / period
        return ma
    
    
    def sma_crossover_strategy(self):    
        maShort = Sma.calculate_ma(data, mt5.short_Period)
        maLong = Sma.calculate_ma(data, mt5.long_Period)
        try:
            if maShort > maLong:
                return "BUY"
            elif maShort < maLong:
                return "SELL"
            else:
                return "HOLD"
        #this can probably be classed off or made its own function
        except:
            print("error in your logic")
         
        else:
            print("no error")
         
        finally:
            print("Symbol:", Trade.symbol)
            print("Number of trades:", Trade.totalTrades)
            print("Winning trades:",Trade.winningTrades)
            print("Losing trades:", Trade.losingTrades)
            print("Win rate:", round((Trade.winningTrades / Trade.totalTrades) * 100, 2), "%")
            print("Total profit (in points):", round(Trade.profit, 2))

data = yf.download("YM", start='2021-01-01', end='2023-01-01')
      
YM = Sma("@YM", Trade.timeFrame, 5000, mt5.copy_rates_from("YM", Trade.timeFrame, datetime.datetime.now(), 5000))


YM.sma_crossover_strategy()