
import yfinance as yf
yf.pdr_override()


start_date = "2020-01-01"
end_date = "2020-12-31"
ticker = 'TSLA'
data = pdr.get_data_yahoo(ticker,start=start_date, end=end_date)
print(data)

close = data['Close']
ax = close.plot(title='Tesla')
ax.set_xlabel('Date')
ax.set_ylabel('Close')
ax.grid()
plt.show()