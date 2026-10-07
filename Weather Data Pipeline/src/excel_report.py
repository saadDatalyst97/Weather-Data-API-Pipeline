import pandas as pd

# Load cleaned data
file_path = "data/cleaned/cleaned_weather_data.csv"
df = pd.read_csv(file_path)

# Create Excel file
output_path = "excel/weather_analysis.xlsx"

with pd.ExcelWriter(output_path, engine="openpyxl") as writer:

    # Sheet 1: Weather Data
    df.to_excel(writer, sheet_name="Weather Data", index=False)

    # Sheet 2: Summary
    summary = pd.DataFrame({
        "Metric": [
            "Average Temperature",
            "Highest Temperature",
            "Lowest Temperature",
            "Average Humidity",
            "Highest Humidity",
            "Average Wind Speed"
        ],
        "Value": [
            df["temperature"].mean(),
            df["temperature"].max(),
            df["temperature"].min(),
            df["humidity"].mean(),
            df["humidity"].max(),
            df["wind_speed"].mean()
        ]
    })

    summary.to_excel(writer, sheet_name="Summary", index=False)

print("Excel report generated successfully!")
print("File:", output_path)