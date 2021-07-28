# stockcandle

A utility to fetch intraday data for any given EQ symbol. 


## Installation
```
pip install stockcandle
```

## Usage
```
from stockcandle import DataCollector

dataClass = DataCollector()

# Fetch LTP data for the day
ltp_data = dataClass.intraday_data('RELIANCE')
print(ltp_data)

# Fetch minute period candle for the intraday
candle_data = dataClass.intraday_candle('TATAMOTORS')
print(candle_data)

```

## Response

1> ltp_data = dataClass.intraday_data('RELIANCE')
```
...., 
{'timestamp': datetime.datetime(2021, 7, 27, 14, 49, 51), 'ltp': 2047.95}, 
{'timestamp': datetime.datetime(2021, 7, 27, 14, 49, 52), 'ltp': 2047.95}, 
{'timestamp': datetime.datetime(2021, 7, 27, 14, 49, 54), 'ltp': 2047.95}, 
{'timestamp': datetime.datetime(2021, 7, 27, 14, 49, 55), 'ltp': 2048}, 
{'timestamp': datetime.datetime(2021, 7, 27, 14, 49, 56), 'ltp': 2048.3}, 
{'timestamp': datetime.datetime(2021, 7, 27, 14, 49, 57), 'ltp': 2048.3}, 
{'timestamp': datetime.datetime(2021, 7, 27, 14, 49, 58), 'ltp': 2048.3}, 
{'timestamp': datetime.datetime(2021, 7, 27, 14, 49, 59), 'ltp': 2048.3},
....
```

2> candle_data = dataClass.intraday_candle('TATAMOTORS')
```
....
'2021-07-28 12:45:00': {'open': 285.25, 'high': 285.5, 'low': 285.15, 'close': 285.25}, 
'2021-07-28 12:46:00': {'open': 285.25, 'high': 285.45, 'low': 285.1, 'close': 285.45}, 
'2021-07-28 12:47:00': {'open': 285.45, 'high': 285.55, 'low': 285.35, 'close': 285.4}, 
'2021-07-28 12:48:00': {'open': 285.35, 'high': 285.35, 'low': 285.15, 'close': 285.25}, 
'2021-07-28 12:49:00': {'open': 285.25, 'high': 285.6, 'low': 285.2, 'close': 285.55}, 
'2021-07-28 12:50:00': {'open': 285.65, 'high': 285.7, 'low': 285.4, 'close': 285.7}, 
'2021-07-28 12:51:00': {'open': 285.7, 'high': 285.75, 'low': 285.5, 'close': 285.55},
....
```