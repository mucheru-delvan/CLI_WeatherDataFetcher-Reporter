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
    
    def analyze_data(self,data):
        highest_temp = max(day['day']['maxtemp_c'] for day in data['forecast']['forecastday'])
        average_humidity = sum(day['day']['avghumidity'] for day in data['forecast']['forecastday']) / len(data['forecast']['forecastday'])
        day_with_most_rain = max(data['forecast']['forecastday'], key=lambda day: day['day']['totalprecip_mm'])['date']

        return highest_temp, average_humidity, day_with_most_rain

    def write_weather_report_txt(self, data):

        location = data.get("location", {})
        city = location.get("name", "unknown").lower()
        filename = f"{city}_weather_report.txt"

        highest_temperature,past_average_humidity, day_with_most_rain = self.analyze_data(data)

        lines = [
            "WEATHER REPORT",
            "=" * 30,
            "",
            f"Location     : {location.get('name', 'N/A')}, {location.get('country', 'N/A')}",
            f"Local Time   : {location.get('localtime', 'N/A')}",
            "",
            f"Highest Temperature for the past 7 days : {highest_temperature} °C",
            f"Average Humidity for the past 7 days    : {past_average_humidity:.2f}%",
            f"Day with Most Precipitation  : {day_with_most_rain}",
        ]

        with open(filename, "w", encoding="utf-8") as file:
            file.write("\n".join(lines))

        print(f"Saved report as {filename}")

