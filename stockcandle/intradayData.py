
"""
@author: rakeshr
"""

"""
Fetch intraday LTP data for the day and calculate OHLC candle
"""

import requests
import datetime


class DataCollector():

    def __init__(self, symbol):
        self.symbol = symbol
        self.chart_url = 'https://www.nseindia.com/api/chart-databyindex?'
        self.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        self.nse_referer = 'https://www.nseindia.com/get-quotes/equity?symbol={}'.format(self.symbol)
        self.header_ref = {'User-Agent': self.user_agent, 'referer': self.nse_referer ,'accept': "application/json", 
        'x-requested-with': "XMLHttpRequest",'sec-fetch-mode':"cors", 'sec-fetch-site':"same-origin"}

    def intraday_data(self):
        """
        Fetch intraday data for the day of requested EQ symbol
        """
        param = {
            'index': "{}EQN".format(self.symbol)
        }
        request_sess = requests.Session()
        response = request_sess.get(self.chart_url, headers= self.header_ref, params = param)

        # Set start_time as market start time i.e 09:00:00 AM
        start_time = datetime.datetime.today().replace(hour=9, minute=0, second=0, microsecond=0)
        intra_data = []
        for value in response.json()['grapthData']:
            # Encode the grapth Data for time object
            # 1627376400000 = 9:00:00 AM 
            second_diff = (value[0] - 1627376400000)/1000
            tick_time = start_time + datetime.timedelta(seconds=second_diff)
            intra_data.append({'time': tick_time, 'ltp':value[1]})
        
        return intra_data
        