"""
data_collection.py
Collects current weather data for major Pakistani cities using the
Open-Meteo API (free, no API key required).
"""

import requests
import pandas as pd
from datetime import datetime

# City coordinates (latitude, longitude)
CITIES = {
    "Karachi": (24.8607, 67.0011),
    "Lahore": (31.5497, 74.3436),
    "Islamabad": (33.6844, 73.0479),
    "Rawalpindi": (33.5651, 73.0169),
    "Peshawar": (34.0151, 71.5249),
    "Quetta": (30.1798, 66.9750),
    "Multan": (30.1575, 71.5249),
    "Astore": (35.3463, 74.8638),
}

BASE_URL = "https://api.open-meteo.com/v1/forecast"

# WMO weather codes -> human-readable condition (subset commonly returned)
WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Fog", 48: "Depositing rime fog",
    51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
    61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
    71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow",
    80: "Slight rain showers", 81: "Moderate rain showers", 82: "Violent rain showers",
    95: "Thunderstorm",
}


def fetch_weather(city_name: str, lat: float, lon: float) -> dict:
    """Fetch current weather for a single city from Open-Meteo."""
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,relative_humidity_2m,surface_pressure,wind_speed_10m,weather_code",
        "timezone": "auto",
    }
    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()["current"]

    return {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "city": city_name,
        "temperature": data.get("temperature_2m"),
        "humidity": data.get("relative_humidity_2m"),
        "pressure": data.get("surface_pressure"),
        "wind_speed": data.get("wind_speed_10m"),
        "weather_condition": WEATHER_CODES.get(data.get("weather_code"), "Unknown"),
    }


def collect_all_cities() -> pd.DataFrame:
    """Fetch weather data for all configured cities and return as a DataFrame."""
    records = []
    for city, (lat, lon) in CITIES.items():
        try:
            records.append(fetch_weather(city, lat, lon))
        except requests.RequestException as e:
            print(f"Failed to fetch data for {city}: {e}")
    return pd.DataFrame(records)


if __name__ == "__main__":
    df = collect_all_cities()
    df.to_csv("data/raw/weather_data.csv", index=False)
    print(f"Saved {len(df)} records to data/raw/weather_data.csv")
    print(df)