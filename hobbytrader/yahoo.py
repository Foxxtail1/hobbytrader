import re
import pandas as pd
import yfinance as yf
import datetime

from datetime import datetime, date


def daily_prices(tickers):
    # Sanity checks, return None if failed
    if not isinstance(tickers, list):
        return None
    if len(tickers) <= 1:
        return None
    
    data = yf.download(tickers, period='5y', interval='1d')
    data = data.loc[(slice(None)),(slice(None),slice(None))].copy()
    data = data.stack()
    data = data.reset_index()
    data.rename(columns={'level_1': 'Symbol'}, inplace=True)
    data.set_index('Date', inplace=True)
    return data


# def yahoo_prices(tickers, current_day=None):
#     # Sanity checks, return None if failed
#     if not isinstance(tickers, list):
#         return None
#     if len(tickers) <= 1:
#         return None
#     if not isinstance(current_day, str):
#         return None
#     regex = r"^\d{4}-\d{2}-\d{2}$"          # Date format 2023-01-01
#     if not re.match(regex, current_day): 
#         return None
    
#     # Return a DataFrame with dates, symbols and prices
#     years_back = 5
#     end_dt = datetime.strptime(current_day, '%Y-%m-%d').date()
# #    if not isinstance(end_dt, datetime.date):
# #        return None
    
#     start_dt = date(end_dt.year - years_back, end_dt.month, end_dt.day)

#     #data = yf.download(tickers, start=start_dt, end=end_dt)
#     data = yf.download(tickers)
#     data = data.loc[(slice(None)),(slice(None),slice(None))].copy()
#     data = data.stack()
#     data = data.reset_index()
#     data.rename(columns={'level_1': 'Symbol'}, inplace=True)
#     data.set_index('Date', inplace=True)
#     return data

def minute_prices(tickers):
    if not isinstance(tickers,list):
        return None
    if len(tickers) <= 1:
        return None
    
    data = yf.download(tickers, period='1d', interval="1m", ignore_tz = True, prepost=False)
    
    data = data.loc[(slice(None)),(slice(None),slice(None))].copy()
    data = data.stack()
    data = data.reset_index()
    data.rename(columns={'level_1': 'Symbol'}, inplace=True)
    data.rename(columns={'level_0': 'Datetime'}, inplace=True)
    data.set_index('Datetime', inplace=True)
    return data


if __name__ == '__main__':
    symbols = ['MSFT', 'AMZN']
    #data = yahoo_prices(symbols, '2023-03-26')
    data = daily_prices(symbols)
    #data = yf.download(symbols, period='5y', interval='1d')
    print(data)

