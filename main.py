import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt


# kaggle: https://www.kaggle.com/sudalairajkumar/cryptocurrencypricehistory?select=coin_Dogecoin.csv
# what is crypto market cap: Crypto market capitalization is the total value of a cryptocurrency. Where stock market capitalization is calculated by multiplying share price times shares outstanding, crypto market capitalization is calculated by multiplying the price of the cryptocurrency with the number of coins in circulation.
# https://time.com/nextadvisor/investing/cryptocurrency/what-is-crypto-market-cap/
# Q: How did market capitalizations of dogecoin change over time?


dogecoin_data = pd.read_csv('coin_Dogecoin.csv', parse_dates=['Date'])
print(dogecoin_data.dtypes)


market_cap = dogecoin_data['Market_cap']
print(market_cap.head())

dates = dogecoin_data['Date']
print(dates.head())

high = dogecoin_data['High']
print(high.head())

low = dogecoin_data['Low']
print(low.head())

volume = dogecoin_data['Volume']
print(volume.head())

left = dt.date(2021, 1, 10)
right = dt.date(2021, 6, 10)

plt.scatter(dates,market_cap, color='green')
plt.title('Dogecoin: Market Capitalisation [2021]', fontsize=12)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Market Cap [USD]', fontsize=12)
plt.gca().set_xbound(left, right)
plt.show()


plt.bar(dates,volume, color='teal')
plt.title('Dogecoin: Volume of Transactions [2021]', fontsize=12)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Volume', fontsize=12)
plt.gca().set_xbound(left, right)
plt.show()


plt.bar(dates, high, label="High")
plt.bar(dates, low, color= "orange", label="Low")
plt.legend()
plt.title('Dogecoin: Comparison of Lows and Highs on a Given Day [2021]', fontsize=12)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price [USD]', fontsize=12)
plt.gca().set_xbound(left, right)
plt.show()
