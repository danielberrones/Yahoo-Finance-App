import yfinance as yf


userTicker = input("Enter ticker symbol: ")
userTicker = yf.Ticker(userTicker)
for k,v in userTicker.info.items():
        print(k,v)