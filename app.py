from sqlite3 import Timestamp
import requests
import json
import time
from datetime import date, datetime, timedelta

## make automatic for day before being used

todays_date = datetime.today()
yesterday = todays_date - timedelta(days=1)
newdate = yesterday.replace(hour=0, minute=0)
unixtime = time.mktime(newdate.timetuple())
# print(todays_date)
# print(yesterday)
# print(newdate)
print(unixtime)

r = requests.get('https://api.kucoin.com/api/v1/market/candles?type=1min&symbol=BTC-USDT&startAt=1657274400&endAt=1657360800')
# print(r)

string = r.text
# print(string)

dic = json.loads(string)
# print(dic)

candles = dic['data']
# print(x)
# print(type(x))
# print(len(candles))

# print(candles[0])
# dt = datetime.fromtimestamp(int(candles[0][0]))
# ts = datetime(2022,7,8,0,0,0).timestamp()
# print(ts + 86400)
# print(dic.keys())