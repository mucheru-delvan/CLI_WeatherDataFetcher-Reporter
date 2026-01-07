import requests
from config import API_KEY, BASE_URL

class WeatherFetcher:
    def __init__(self, api_key=API_KEY, base_url=BASE_URL):
        self.api_key = api_key
        self.base_url = base_url

    def fetch_weather_data(self, city_name):
        params = {
            'key': self.api_key,
            'q': city_name
        }

        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            return {'error': 'City not found or API request failed.'}