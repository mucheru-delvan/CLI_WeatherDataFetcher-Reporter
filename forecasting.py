from config import API_KEY, BASE_URL

def get_forecast_url(city_name, days=3):
    return f"{BASE_URL.replace('current', 'forecast')}?key={API_KEY}&q={city_name}&days={days}"

def parse_forecast_data(data):
    forecast_days = data.get("forecast", {}).get("forecastday", [])
    parsed_data = []

    for day in forecast_days:
        date = day.get("date", "N/A")
        day_info = day.get("day", {})
        condition = day_info.get("condition", {}).get("text", "N/A")
        max_temp = day_info.get("maxtemp_c", "N/A")
        min_temp = day_info.get("mintemp_c", "N/A")
        avg_humidity = day_info.get("avghumidity", "N/A")

        parsed_data.append({
            "date": date,
            "condition": condition,
            "max_temp": max_temp,
            "min_temp": min_temp,
            "avg_humidity": avg_humidity
        })

    return parsed_data


print(parse_forecast_data({"forecast": {"forecastday": [{"date": "2024-04-05", "day": {"condition": {"text": "Sunny"}, "maxtemp_c": 20, "mintemp_c": 10, "avghumidity": 60}}]} }))

print(get_forecast_url("Nairobi", days=3))