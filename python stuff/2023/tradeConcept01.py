symbol = "@YM"
timeframe = mt5.TIMEFRAME_M1

num_candles = 5000

rates = mt5.copy_rates_from(symbol, timeframe, datetime.datetime.now(), num_candles)
close_prices = [candle[4] for candle in rates]


short_ma_period = 10
long_ma_period = 20


total_trades = 0
winning_trades = 0
losing_trades = 0
profit = 0.0

in_position = False
entry_price = 0.0


if not mt5.initialize():
    print("Initialization failed!")
    mt5.shutdown()
    exit()



if rates is None:
    print("Failed to retrieve historical data.")
    mt5.shutdown()
    exit()




def calculate_ma(data, period):
    ma = sum(data[-period:]) / period
    return ma


def sma_crossover_strategy(data, short_period, long_period):
    ma_short = calculate_ma(data, short_period)
    ma_long = calculate_ma(data, long_period)

    if ma_short > ma_long:
        return "BUY"
    elif ma_short < ma_long:
        return "SELL"
    else:
        return "HOLD"


for i in range(long_ma_period, len(close_prices)):
    signal = sma_crossover_strategy(close_prices[:i], short_ma_period, long_ma_period)
    current_price = close_prices[i]

    if signal == "BUY" and not in_position:
        total_trades += 1
        in_position = True
        entry_price = current_price
    elif signal == "SELL" and in_position:
        in_position = False
        if current_price > entry_price:
            winning_trades += 1
            profit += (current_price - entry_price)
        else:
            losing_trades += 1
            profit -= (current_price - entry_price)



# Display backtest results
print("Symbol:", symbol)
print("Number of trades:", total_trades)
print("Winning trades:", winning_trades)
print("Losing trades:", losing_trades)
print("Win rate:", round((winning_trades / total_trades) * 100, 2), "%")
print("Total profit (in points):", round(profit, 2))
