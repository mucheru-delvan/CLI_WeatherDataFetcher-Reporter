

# Weather History Analyzer

A small Python utility that fetches **historical weather data for the past 7 days** for a given city, analyzes it, and generates a **plain-text weather report**.

## What This Project Does (Fact, Not Hype)

* Fetches **past 7 days of weather history** for a city using a weather API
* Computes:

  * Highest temperature recorded
  * Average humidity
  * Day with the most rainfall
* Saves the results to a **`.txt` report file**

This is **not** a forecasting tool. It is strictly historical analysis.

---

## Requirements

* Python 3.8+
* `requests` library

Install dependencies:

```bash
pip install requests
```

---

## Configuration

Create a `config.py` file in the project root:

```python
API_KEY = "your_api_key_here"
BASE_URL = "https://api.weatherapi.com/v1/history.json"
```

This project assumes:

* The API supports historical queries via a `dt` parameter
* The response contains `forecast.forecastday[0]`

If either assumption breaks, the code will fail silently (by design — see critique below).

---

## Usage

Example usage in another Python file or an interactive session:

```python
from weather_fetcher import WeatherFetcher

wf = WeatherFetcher()
history = wf.fetch_past_7_days("London")

if history:
    wf.write_weather_report_txt("London", history)
```

---

## Output

A text file named:

```
<City>_weather_history_report.txt
```

Example contents:

```
WEATHER HISTORY REPORT (PAST 7 DAYS)
========================================

Location                    : London
Highest Temperature         : 24.5 °C
Average Humidity            : 67.32 %
Day with Most Precipitation : 2026-01-10
```

---

## Design Notes (What This Project Assumes)

* Missing days due to API errors are **ignored**, not retried
* Analysis assumes **at least one valid day** exists
* Temperatures are handled in **Celsius only**
* No timezone handling is performed

---

## Limitations (Be Honest)

* No logging — failures are swallowed silently
* No input validation for city names
* No unit tests
* API schema is hard-coded
* Not suitable for large-scale or production use

---

## License

Educational / personal use.

---
