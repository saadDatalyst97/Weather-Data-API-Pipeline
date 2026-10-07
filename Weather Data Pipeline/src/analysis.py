import pandas as pd
import numpy as np

# Load cleaned data
file_path = "data/cleaned/cleaned_weather_data.csv"

df = pd.read_csv(file_path)

# Convert date to datetime
df["date"] = pd.to_datetime(df["date"])

print("\n===== WEATHER DATA ANALYSIS =====")

# Average temperature
average_temperature = np.mean(df["temperature"])
print("\nAverage Temperature:", round(average_temperature, 2), "°C")

# Maximum temperature
max_temperature = np.max(df["temperature"])
max_temp_city = df.loc[df["temperature"].idxmax(), "city"]

print("Highest Temperature:", max_temperature, "°C")
print("City:", max_temp_city)

# Minimum temperature
min_temperature = np.min(df["temperature"])
min_temp_city = df.loc[df["temperature"].idxmin(), "city"]

print("\nLowest Temperature:", min_temperature, "°C")
print("City:", min_temp_city)

# Average humidity
average_humidity = np.mean(df["humidity"])
print("\nAverage Humidity:", round(average_humidity, 2), "%")

# Highest humidity
max_humidity = np.max(df["humidity"])
max_humidity_city = df.loc[df["humidity"].idxmax(), "city"]

print("Highest Humidity:", max_humidity, "%")
print("City:", max_humidity_city)

# Average wind speed
average_wind = np.mean(df["wind_speed"])
print("\nAverage Wind Speed:", round(average_wind, 2), "m/s")

# Weather conditions
print("\nWeather Conditions:")
print(df["weather_condition"].value_counts())

# Complete summary
print("\n===== SUMMARY STATISTICS =====")
print(df[["temperature", "humidity", "pressure", "wind_speed"]].describe())