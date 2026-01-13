
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

forecast_data = get_forecast_url('London', 1)
data = list(forecast_data['forecast']["forecastday"])
# Print the keys of the forecast data
pprint(data[0]['day'])

