import yfinance as yf
import pandas as pd

def get_data(ticker: str, 
             start_date: str, 
             end_date: str, 
             interval: str ='1m') -> pd.DataFrame:
    data = yf.download(ticker,
                       start_date,
                       end_date,
                       interval=interval)
    return data

def get_returns(data: pd.DataFrame) -> pd.DataFrame:
    data['returns'] = data['Close'].pct_change()
    data['returns'] = data['returns']
    return data

def get_list_of_days(data: pd.DataFrame) -> pd.DataFrame:
    list_of_days = []
    for i in range(10, len(data)):
        list_of_days.append(data['returns'][i-10:i].tolist())
    return pd.DataFrame(list_of_days)

