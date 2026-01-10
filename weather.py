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
         

        try:
            response = requests.get(self.base_url, params=params)

            response.raise_for_status()
            return response.json()
    
        except requests.exceptions.RequestException as e:
            return {'error': str(e)} 

    def display_weather(self, data):
        location = data["location"]
        current = data["current"]

        city = location["name"]
        country = location["country"]
        local_time = location["localtime"]

        temp = current["temp_c"]
        
        condition = current["condition"]["text"]
        humidity = current["humidity"]
        wind_speed = current["wind_kph"]
        wind_dir = current["wind_dir"]
        is_day = current["is_day"]

        time_icon = "☀️" if is_day == 1 else "🌙"

        print("\n🌤️ Weather Report 🌤️")
        print(f"City: {city}, {country}")
        print(f"Local Time: {local_time}\n")
        print(f"Temperature: {temp}°C (Feels like {feels_like}°C)")
        print(f"Condition: {condition} {time_icon}")
        print(f"Humidity: {humidity}%")
        print(f"Wind: {wind_speed} km/h ({wind_dir})")

            
    