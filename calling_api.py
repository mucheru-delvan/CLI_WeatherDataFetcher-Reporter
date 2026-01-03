import requests

def fetch_weather_data(city_name):
    
    api_key = 'f22f72d06e204caab4874935260301'
    base_url = 'https://api.weatherapi.com/v1/current.json'

    params = {
        'key': api_key,
        'q': city_name
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'City not found or API request failed.'}

print(fetch_weather_data('London'))
print(fetch_weather_data('New York'))   

