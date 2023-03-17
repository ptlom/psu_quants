# -*- coding: utf-8 -*-
"""montecarlo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JkyH3ETDM8xlvArStOiw0vi2AD8Id7Y2
"""

# Commented out IPython magic to ensure Python compatibility.
!pip install yfinance 
import math 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf 
import datetime 
yf.pdr_override()
# %matplotlib inline

stock = pdr.get_data_yahoo("SIVB", start = "2020-1-1", end = "2023-2-22")

stock.head()

"""![image.png](data:image/png;base64,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)

Wiener Process: The returns of the portfolio are a Wiener process, in which 
volatility scales with the square-root of time.

Advanced calculus process, but just know that for a lot of quant stuff volatility scales with the sqrt of time (Sharpe ratios etc.)
Therefore in order to annualize the standard deviation we need to multiply it by sqrt(250)
"""

time_elapsed = (stock.index[-1] - stock.index[0]).days
#get the total growth rate
total_growth = (stock['Adj Close'][-1] / stock['Adj Close'][1])



#convert days into years
number_of_years = time_elapsed / 365.0


#Second, we can raise the total growth to the inverse of the # of years
#this provides the "cagr"
cagr = total_growth ** (1/number_of_years) - 1

#get standard deviation so we can construct a probability distribution 
std_dev = stock['Adj Close'].pct_change().std()

#Next, because there are 250 trading days in a year,
std_dev = std_dev * math.sqrt(250)

#From here, we have our two inputs needed to generate random
#values in our simulation
print ("cagr (mean returns) : ", str(round(cagr,4)))
print ("std_dev (standard deviation of return : )", str(round(std_dev,4)))

"""

1.   List item
2.   List item

"""

#using numpy and assuming a normal distribution
number_of_trading_days = 250
daily_return_percentages = np.random.normal(cagr/number_of_trading_days, std_dev/math.sqrt(number_of_trading_days), number_of_trading_days) + 1 


#create a random walk -- we have a random probability distribution, so apply it to the adjusted close price
price_series = [stock['Adj Close'][-1]]

for i in daily_return_percentages:
    price_series.append(price_series[-1] * i)

#Now we have some randomized daily return percentages
plt.plot(daily_return_percentages)
plt.show()



#Great, now we can plot a single 'random walk' of stock prices
plt.plot(price_series)
plt.show()

#A Monte Carlo method would do this THOUSANDS, hundreds of thousands, millions of times
number_of_trials = 10000


closing_prices = [] 

for i in range(number_of_trials):
    #Copy and paste code for 1 year from above, and repeat this for each trial 
    daily_return_percentages = np.random.normal(cagr/number_of_trading_days, std_dev/math.sqrt(number_of_trading_days), number_of_trading_days) + 1 
    price_series = [stock['Adj Close'][-1]]

    for j in daily_return_percentages:
        price_series.append(price_series[-1] * j)

    #append closing prices in last day of window for histogram
    closing_prices.append(price_series[-1])

    #plot all random walks
    plt.plot(price_series)

plt.show()

#plot histogram
plt.hist(closing_prices,bins=50)

plt.show()

#lastly, we can split the distribution into percentiles
#to help us gauge risk vs. reward

#Pull top 10% of possible outcomes
top_ten = np.percentile(closing_prices,100-10)

#Pull bottom 10% of possible outcomes
bottom_ten = np.percentile(closing_prices,10);

mean_end_price = round(np.mean(closing_prices),2)

#create histogram again
plt.hist(closing_prices,bins=40)
#append w/ top 10% line
plt.axvline(top_ten,color='r',linestyle='dashed',linewidth=2)
#append w/ bottom 10% line
plt.axvline(bottom_ten,color='r',linestyle='dashed',linewidth=2)
#append with current price
plt.axvline(stock['Adj Close'][-1],color='g', linestyle='dashed',linewidth=2)
#-1 just gets the last member of the df
#append with mean end price 
plt.axvline(mean_end_price, color = 'm', linestyle = 'solid', linewidth = 2)
plt.show()
print(f'90th percentile price:{str(round(top_ten))}')
print(f'10th percentile price:{str(round(bottom_ten))}')
print(f'Mean price: {str(round(mean_end_price))}')

"""Buy or sell?

Positive skew? What does it mean?

"""