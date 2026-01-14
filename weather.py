import requests
from datetime import datetime, timedelta
from config import API_KEY ,BASE_URL

class WeatherFetcher:

    def __init__(self, api_key=API_KEY, base_url=BASE_URL):
        self.api_key = api_key
        self.base_url = base_url

    def fetch_past_7_days(self, city_name):
        today = datetime.today()
        history_days = []

        for i in range(1, 8):
            date = (today - timedelta(days=i)).strftime("%Y-%m-%d")

            params = {
                "key": self.api_key,
                "q": city_name,
                "dt": date
            }

            try:
                response = requests.get(self.base_url, params=params)
                response.raise_for_status()
                data = response.json()
                history_days.append(data["forecast"]["forecastday"][0])
            except requests.exceptions.RequestException:
                continue

        return history_days

    def analyze_history(self, history_days):
        highest_temp = max(d["day"]["maxtemp_c"] for d in history_days)
        average_humidity = (
            sum(d["day"]["avghumidity"] for d in history_days)
            / len(history_days)
        )
        day_with_most_rain = max(
            history_days,
            key=lambda d: d["day"]["totalprecip_mm"]
        )["date"]

        return highest_temp, average_humidity, day_with_most_rain

    def write_weather_report_txt(self, city_name, history_days):
        highest, avg_humidity, rain_day = self.analyze_history(history_days)
        filename = f"{city_name.title()}_weather_history_report.txt"

        lines = [
            "WEATHER HISTORY REPORT (PAST 7 DAYS)",
            "=" * 40,
            "",
            f"Location                    : {city_name}",
            f"Highest Temperature         : {highest} °C",
            f"Average Humidity            : {avg_humidity:.2f} %",
            f"Day with Most Precipitation : {rain_day}",
        ]

        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        print(f"Saved report as {filename}")
        return filename
