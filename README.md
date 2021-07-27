# stockcandle

A utility to fetch intraday data for any given EQ symbol. 


## Installation
```
pip install stockcandle
```

## Usage
```
from stockcandle import DataCollector

dataClass = DataCollector('RELIANCE')
ltp_dump = dataClass.intraday_data()
print(ltp_dump)
```

## Response

```
...., {'timestamp': datetime.datetime(2021, 7, 27, 14, 49, 51), 'ltp': 2047.95}, {'timestamp': datetime.datetime(2021, 7, 27, 14, 49, 52), 
'ltp': 2047.95}, {'timestamp': datetime.datetime(2021, 7, 27, 14, 49, 54), 'ltp': 2047.95}, 
{'time': datetime.datetime(2021, 7, 27, 14, 49, 55), 'ltp': 2048}, {'timestamp': datetime.datetime(2021, 7, 27, 14, 49, 56), 
'ltp': 2048.3}, {'timestamp': datetime.datetime(2021, 7, 27, 14, 49, 57), 'ltp': 2048.3}, 
{'timestamp': datetime.datetime(2021, 7, 27, 14, 49, 58), 'ltp': 2048.3}, {'timestamp': datetime.datetime(2021, 7, 27, 14, 49, 59), 
'ltp': 2048.3}, {'timestamp': datetime.datetime(2021, 7, 27, 14, 50), 'ltp': 2048.3}, 
{'timestamp': datetime.datetime(2021, 7, 27, 14, 50, 1), 'ltp': 2048.3}, {'timestamp': datetime.datetime(2021, 7, 27, 14, 50, 3), 
'ltp': 2048.25}, {'timestamp': datetime.datetime(2021, 7, 27, 14, 50, 5), 'ltp': 2048.5}, 
{'timestamp': datetime.datetime(2021, 7, 27, 14, 50, 6), 'ltp': 2048.25}, {'timestamp': datetime.datetime(2021, 7, 27, 14, 50, 7), 'ltp': 2048.45}, 
{'timestamp': datetime.datetime(2021, 7, 27, 14, 50, 8), 'ltp': 2048.4},...
```