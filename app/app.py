import yfinance as yf

# GOOG = Google
# APPL = Apple
# DASH = DoorDash
# NFLX = Netflix
# TSLA = Tesla

userTicker = input("Enter ticker symbol: ")
userTicker = yf.Ticker(userTicker)
for k,v in userTicker.info.items():
    if k == "longBusinessSummary":
        with open('longBusinessSummary.txt','w') as f:
                f.write(str(v))


