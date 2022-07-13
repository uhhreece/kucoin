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
start = unixtime - 86400

# print(todays_date)
# print(yesterday)
# print(newdate)
# print(unixtime)

r = requests.get(f'https://api.kucoin.com/api/v1/market/candles?type=1min&symbol=BTC-USDT&startAt={int(start)}&endAt={int(unixtime)}')
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
dt = datetime.fromtimestamp(int(candles[0][0]))
dt2 = datetime.fromtimestamp(int(candles[-1][0]))
ts = dt.timestamp()
print(dt)
print(dt2)
print(datetime.fromtimestamp(int(ts + 86400)))
print(dic.keys())
print(candles.__len__())