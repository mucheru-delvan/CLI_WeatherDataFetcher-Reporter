import requests

def fetch_weather_data(city_name):


    api_key    = 'your_api_key_here'    base_url   = 'http://api.openweathermap.org/data/2.5/weather'    params     = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }    response  = requests.get(base_url, params=params)    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'City not found or API request failed.'}    api_key = 'your_api_key_here'  base_url = 'http://api.openweathermap.org/data/2.5/weather'    params = {       'q': city_name,                                                     
                                                                                                                                                                             