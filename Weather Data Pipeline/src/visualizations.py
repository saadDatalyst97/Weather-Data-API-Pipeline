import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
file_path = "data/cleaned/cleaned_weather_data.csv"
df = pd.read_csv(file_path)


# 1. Temperature by City
plt.figure(figsize=(10, 6))
plt.bar(df["city"], df["temperature"])
plt.title("Temperature by City")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualizations/temperature_by_city.png")
plt.close()


# 2. Humidity by City
plt.figure(figsize=(10, 6))
plt.bar(df["city"], df["humidity"])
plt.title("Humidity by City")
plt.xlabel("City")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualizations/humidity_by_city.png")
plt.close()


# 3. Wind Speed by City
plt.figure(figsize=(10, 6))
plt.bar(df["city"], df["wind_speed"])
plt.title("Wind Speed by City")
plt.xlabel("City")
plt.ylabel("Wind Speed (m/s)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualizations/wind_speed_by_city.png")
plt.close()


# 4. Weather Conditions
weather_counts = df["weather_condition"].value_counts()

plt.figure(figsize=(8, 6))
plt.pie(
    weather_counts,
    labels=weather_counts.index,
    autopct="%1.1f%%"
)
plt.title("Weather Conditions Distribution")
plt.tight_layout()
plt.savefig("visualizations/weather_conditions.png")
plt.close()


print("All charts generated successfully!")