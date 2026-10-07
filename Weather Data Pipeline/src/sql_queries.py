import sqlite3
import pandas as pd

conn = sqlite3.connect("data/weather.db")

print("\n===== SQL-BASED WEATHER ANALYSIS =====")

# 1. Average temperature and humidity per city
query1 = """
SELECT city,
       ROUND(AVG(temperature), 2) AS avg_temperature,
       ROUND(AVG(humidity), 2) AS avg_humidity
FROM weather
GROUP BY city
ORDER BY avg_temperature DESC;
"""
print("\nAverage Temperature & Humidity by City:")
print(pd.read_sql_query(query1, conn))

# 2. City with the highest recorded temperature
query2 = """
SELECT city, temperature
FROM weather
ORDER BY temperature DESC
LIMIT 1;
"""
print("\nHighest Temperature Recorded:")
print(pd.read_sql_query(query2, conn))

# 3. City with the lowest recorded temperature
query3 = """
SELECT city, temperature
FROM weather
ORDER BY temperature ASC
LIMIT 1;
"""
print("\nLowest Temperature Recorded:")
print(pd.read_sql_query(query3, conn))

# 4. Count of records per weather condition
query4 = """
SELECT weather_condition, COUNT(*) AS record_count
FROM weather
GROUP BY weather_condition
ORDER BY record_count DESC;
"""
print("\nWeather Condition Frequency:")
print(pd.read_sql_query(query4, conn))

# 5. Weather trend by date (city-wise average temperature per date)
query5 = """
SELECT date, city, temperature
FROM weather
ORDER BY date, city;
"""
print("\nTime-based Weather Trend:")
print(pd.read_sql_query(query5, conn))

conn.close()
