import requests
from config import API_KEY, BASE_URL

class WeatherFetcher:
    def __init__(self, api_key=API_KEY, base_url=BASE_URL):
        self.api_key = api_key
        self.base_url = base_url

    def fetch_forecast_data(self, city_name, days=7):
        params = {
            'key': self.api_key,
            'q': city_name,
            'days': days
        }
         

        try:
            response = requests.get(self.base_url, params=params)

            response.raise_for_status()
            return response.json()
    
        except requests.exceptions.RequestException as e:
            return {'error': str(e)} 
    

