
"""
@author: rakeshr
"""

"""
Fetch intraday LTP data for the day and calculate OHLC candle
"""

import requests
import datetime


class DataCollector():

    def __init__(self):
        self.chart_url = 'https://www.nseindia.com/api/chart-databyindex?'
        self.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'

    def intraday_data(self, symbol):
        """
        Fetch intraday data for the day of requested EQ symbol
        """
        self.nse_referer = 'https://www.nseindia.com/get-quotes/equity?symbol={}'.format(symbol)
        self.header_ref = {'User-Agent': self.user_agent, 'referer': self.nse_referer ,'accept': "application/json", 
        'x-requested-with': "XMLHttpRequest",'sec-fetch-mode':"cors", 'sec-fetch-site':"same-origin"}

        param = {
            'index': "{}EQN".format(symbol)
        }
        request_sess = requests.Session()
        response = request_sess.get(self.chart_url, headers= self.header_ref, params = param)

        # Set start_time as market start time i.e 09:00:00 AM for encoded graph value(1627376400000)
        start_time = datetime.datetime(2021, 7, 27, 9, 0, 0)
        intra_data = []
        for value in response.json()['grapthData']:
            # Decode the grapth Data for time object
            # 1627376400000 = 9:00:00 AM 
            second_diff = (value[0] - 1627376400000)/1000
            tick_time = start_time + datetime.timedelta(seconds=second_diff)
            intra_data.append({'timestamp': tick_time, 'ltp':value[1]})
        
        return intra_data

    def intraday_candle(self, symbol):
        """
        Create minute candle for the day based on the intraday LTP
        """
        minute_timestamp = datetime.datetime.today().replace(hour=9, minute=15, second=0, microsecond=0)
        minute_dict = {}
        minute_dict[str(minute_timestamp)] = []
        minute_candle = {}

        # Fetch LTP list for the day to create candle
        ltpData = self.intraday_data(symbol) 
        
        for tick in ltpData:
            # Indicates starting of higher new minute candle
            if (tick['timestamp'] - minute_timestamp).seconds > 59:
                # Create OHLC minute candle for the last completed minute period
                minute_candle[str(minute_timestamp)] = {'open': minute_dict[str(minute_timestamp)][0],
                'high': max(minute_dict[str(minute_timestamp)]), 'low': min(minute_dict[str(minute_timestamp)]),
                'close':minute_dict[str(minute_timestamp)][-1]}

                # Update candle period to next minute timestamp
                minute_timestamp = minute_timestamp + datetime.timedelta(seconds=60)
                minute_dict[str(minute_timestamp)] = []

            # Create list of all ltp for that given minute timestamp
            minute_dict[str(minute_timestamp)].append(tick['ltp'])

        return minute_candle
