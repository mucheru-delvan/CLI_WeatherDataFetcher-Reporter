from dbm import error
from weather import WeatherFetcher
from config import DEFAULT_CITY

def main():
    weather_fetcher = WeatherFetcher()

    city_name = input("Enter city name (or press Enter for default city): ").strip()
    if not city_name:
        city_name = DEFAULT_CITY

    data = weather_fetcher.fetch_past_7_days(city_name)

    report_file = weather_fetcher.write_weather_report_txt(city_name, data)

    print(f"\n✅ Weather report saved to {report_file}")


if __name__ == "__main__":
    main()

