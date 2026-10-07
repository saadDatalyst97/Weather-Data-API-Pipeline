import sqlite3
import pandas as pd

# Load cleaned data
file_path = "data/cleaned/cleaned_weather_data.csv"
df = pd.read_csv(file_path)

# Connect to (or create) the SQLite database
conn = sqlite3.connect("data/weather.db")

# Store the DataFrame as a table named 'weather'
df.to_sql("weather", conn, if_exists="replace", index=False)

print("Data successfully stored in data/weather.db (table: weather)")

conn.close()