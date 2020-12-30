import yfinance as yf


userTicker = input("Enter ticker symbol: ")
userTicker = yf.Ticker(userTicker)
for k,v in userTicker.info.items():
    if k == "longBusinessSummary":
        # print(k)
    
        # print(f'KEY:{k}, VALUE:{v}')
        with open('writeMe.txt','w') as f:
                f.write(str(v))


