from weather import WeatherFetcher
from config import DEFAULT_CITY


def display_weather(data):
    location = data["location"]
    current = data["current"]

    city = location["name"]
    country = location["country"]
    local_time = location["localtime"]

    temp = current["temp_c"]
    feels_like = current["feelslike_c"]
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


def main():
    weather_fetcher = WeatherFetcher()

    city_name = input("Enter city name (or press Enter for default city): ").strip()
    if not city_name:
        city_name = DEFAULT_CITY

    data = weather_fetcher.fetch_weather_data(city_name)

    if "error" in data:
        print(f"❌ Error fetching weather data: {data['error']}")
        return

    display_weather(data)


if __name__ == "__main__":
    main()
