import pandas as pd
from pandas_datareader import data
import pandas_datareader as pdr
from tqdm import tqdm
import pickle
# tickers =  pd.read_pickle('Data/sp500Ticker.pickle')

# We would like all available data from 01/01/2000 until 12/31/2016.
start_date = '2009-01-01'
end_date = '2021-12-10'
delete_tickers = []

# # for ticker in tqdm(tickers):
# #     try:
# #         panel_data = data.DataReader(ticker, 'yahoo', start_date, end_date)
# #         panel_data.to_csv('Data/sp500/' + ticker + '.csv')
# #     except:
# #         delete_tickers.append(ticker)
#
# tickers = tickers.remove(delete_tickers)
# print(tickers)
# # tickers.to_pickle('Data/sp500Ticker.pickle',  compression='infer')
# # ticker = '^TNX'
# # panel_data = data.DataReader(ticker, 'yahoo', start_date, end_date)
# # panel_data.to_csv('Data/Bonds/' + ticker + '.csv')

df = pd.read_csv('Data/nasdaq_screener_1639117893902.csv')
tickers = list(df['Symbol'])

# for ticker in tqdm(tickers):
#     try:
#         panel_data = data.DataReader(ticker, 'yahoo', start_date, end_date)
#         panel_data.to_csv('Data/Stocks/nasdaq/' + ticker + '.csv')
#     except:
#         delete_tickers.append(ticker)
#
# with open('Data/ignore-nasdaq.pickle', 'wb') as handle:
#     pickle.dump(delete_tickers, handle, protocol=pickle.HIGHEST_PROTOCOL)
#
# print(delete_tickers)

nasdaq = pdr.DataReader(tickers, data_source='yahoo', start=start_date, end=end_date)
df.to_csv('Data/Nasdaq.csv')
