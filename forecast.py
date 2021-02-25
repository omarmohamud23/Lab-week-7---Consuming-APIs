#Example URL
##http://api.openweathermap.org/data/2.5/weather?q=minneapolis,mn,us&units=imperial&appid=3b376441d9466e7ceb97499d56d61762

import os
import requests
from pprint import pprint
from datetime import datetime


key = os.environ.get('WEATHER_KEY')
query = {'q': 'minneapolis,us', 'units': 'metric', 'appid': key}

 
url = 'http://api.openweathermap.org/data/2.5/forecast'

data = requests.get(url, params=query).json()
pprint(data)

list_of_forecasts = data ['list']

for forecast in list_of_forecasts:
     temp = forecast['main'] ['temp']
     timestamp = forecast['dt'] 
     forecast_date = datetime.fromtimestamp(timestamp)
     print (f'At {forecast_date} the temperature will be {temp} F')


