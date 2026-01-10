from weather import WeatherFetcher
from config import DEFAULT_CITY


def write_weather_report_txt(data):
    location = data.get("location", {})
    current = data.get("current", {})

    city = location.get("name", "unknown").lower()
    filename = f"{city}_weather_report.txt"

    lines = [
        "WEATHER REPORT",
        "=" * 30,
        "",
        f"Location     : {location.get('name', 'N/A')}, {location.get('country', 'N/A')}",
        f"Local Time   : {location.get('localtime', 'N/A')}",
        "",
        f"Temperature  : {current.get('temp_c', 'N/A')} °C",
        f"Feels Like   : {current.get('feelslike_c', 'N/A')} °C",
        f"Condition    : {current.get('condition', {}).get('text', 'N/A')}",
        f"Humidity     : {current.get('humidity', 'N/A')}%",
        f"Wind Speed   : {current.get('wind_kph', 'N/A')} km/h",
    ]

    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))

    print(f"Saved report as {filename}")


def main():
    weather_fetcher = WeatherFetcher()

    city_name = input("Enter city name (or press Enter for default city): ").strip()
    if not city_name:
        city_name = DEFAULT_CITY

    data = weather_fetcher.fetch_weather_data(city_name)

    if "error" in data:
        print(f"❌ Error fetching weather data: {data['error']}")
        return

    write_weather_report_txt(data)

    print("\n✅ Weather report saved to weather_report.txt")


if __name__ == "__main__":
    main()

