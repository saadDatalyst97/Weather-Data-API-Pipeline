import pandas as pd
import os
import pickle
import warnings
warnings.filterwarnings('ignore')

# 1. Load raw data
file_path = "data/raw/weather_data.csv"
df = pd.read_csv(file_path)

print("\nOriginal Data:")
print(df.head())

# 2. Clean data
# Convert Date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# ==========================================
# 🤖 AI INTEGRATION START (The Magic 🪄)
# ==========================================
print("\n🤖 AI Model Load ho raha hai...")
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, '..', 'models', 'MultiCity_Thermal_Model_PRO.pkl')

with open(model_path, 'rb') as f:
    model = pickle.load(f)

expected_columns = model.feature_names_in_

# AI ke liye ek temporary Dataframe banate hain jisme sab values pehle 0 hongi
ai_features = pd.DataFrame(0, index=df.index, columns=expected_columns)

# Date se naye features nikalna
ai_features['Month'] = df['date'].dt.month
ai_features['Hour'] = df['date'].dt.hour

# Purane columns ko naye AI format mein map karna 
# (Agar aapke CSV mein columns ke naam capital hain toh unhe yahan match kar liya gaya hai)
ai_features['Temperature_API'] = df['temperature'] if 'temperature' in df.columns else df['Temperature']
ai_features['Humidity_API'] = df['humidity'] if 'humidity' in df.columns else df['Humidity']
ai_features['WindSpeed_API'] = df['wind_speed'] if 'wind_speed' in df.columns else df['Wind Speed']

# Jo advanced features purane data mein nahi hain, unko default set kar rahe hain taake crash na ho
ai_features['Rain_API'] = 0.0
ai_features['Soil_Temp_API'] = ai_features['Temperature_API'] + 2 # Estimation
ai_features['Solar_Radiation_API'] = 500.0

# City ki One-Hot Encoding Trick
city_column = 'city' if 'city' in df.columns else 'City'
for index, row in df.iterrows():
    city_name = row[city_column]
    city_col_name = f"City_{city_name}"
    if city_col_name in expected_columns:
        ai_features.at[index, city_col_name] = 1

# AI se Predict karwayen aur ORIGINAL data mein naya column add karein
df['AI_Real_Temperature'] = model.predict(ai_features[expected_columns]).round(2)
print("✅ JADOO! AI ne Real Temperature add kar diya hai!")
# ==========================================
# 🤖 AI INTEGRATION END
# ==========================================

# Check data types after cleaning
print("\nData Types After Cleaning & AI:")
print(df.dtypes)

# 3. Save cleaned data
output_path = "data/cleaned/cleaned_weather_data.csv"
df.to_csv(output_path, index=False)

print("\nCleaned & AI-Predicted data saved successfully!")
print("File:", output_path)