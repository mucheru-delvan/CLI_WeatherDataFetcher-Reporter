
import requests
from pprint import pprint
api_key = 'f22f72d06e204caab4874935260301'
base_url = 'https://api.weatherapi.com/v1/forecast.json'


params = {
    'key': api_key,
    'q': '',  
    'days': 0  
        }

def get_forecast_url(city, days):
    response = requests.get(base_url, params={'key': api_key, 'q': city, 'days': days})
    return response.json()

forecast_data = get_forecast_url('London', 7)

forecast_data_seven = forecast_data['forecast']['forecastday']
last_7_days_temps = forecast_data_seven


highest_temp = max(day['day']['maxtemp_c'] for day in last_7_days_temps)
print(f"The highest temperature in the past 7 days in London was: {highest_temp} °C")


