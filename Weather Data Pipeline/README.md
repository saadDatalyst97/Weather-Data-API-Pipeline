# 🌤️ Pakistan Weather Data Analysis & AI Thermal Predictor

An end-to-end Data Engineering, Analytics, and Machine Learning project that analyzes historical and real-time weather conditions across major cities in Pakistan. This project goes beyond descriptive analytics by integrating a trained AI model to predict "Real-Feel" temperatures dynamically.

### 🛠️ Technologies & Stack Used
* **Languages:** Python, SQL (SQLite)
* **Data Collection:** Requests, Open-Meteo API
* **Data Processing & AI Injection:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Random Forest Regressor), Pickle (Model Deployment)
* **Data Storage:** SQLite (`weather.db`)
* **Visualization:** Matplotlib, MS Excel, Power BI

---

## 🚀 Project Workflow

**API Data Extraction** ➡️ **Data Cleaning & AI Prediction (Pandas + Scikit-Learn)** ➡️ **SQL Database Storage** ➡️ **Power BI Dashboard Visualization**

### 1. Data Engineering & Analytics
Weather data is fetched continuously using the Open-Meteo API. The project also handles massive historical data extraction (over 700,000+ rows spanning 10 years) using custom chunking to bypass API rate limits and timeouts.

### 2. Machine Learning Integration (The AI Engine)
A `RandomForestRegressor` model was trained on 10 years of historical Pakistani weather data with an accuracy (R-Squared) of **99.7%** and a Mean Absolute Error (MAE) of **0.50°C**.
* **Seamless Injection:** The trained model (`MultiCity_Thermal_Model_PRO.pkl`) is seamlessly integrated into the data cleaning pipeline (`src/data_cleaning.py`). 
* **Dynamic Prediction:** Before saving to the database, the AI automatically evaluates the raw API data, engineers the required features, and predicts the actual "Real Temperature", appending it as a new column (`AI_Real_Temperature`).

### 3. Database & Visualization
The enriched dataset (API Data + AI Predictions) is stored in a structured SQLite database (`weather.db`). Finally, an interactive **Power BI Dashboard** visualizes time-based weather trends, extreme temperatures, and compares API temperature against the AI's real-feel predictions.

---

## 📁 Project Structure

Weather Data Analysis/
│
├── data/
│   ├── cleaned/
│   │   └── cleaned_weather_data.csv     # Final enriched data with AI Predictions
│   └── raw/
│       ├── weather_data.csv             # Raw API fetch
│       └── weather.db                   # SQLite Database
│
├── excel/
│   └── weather_analysis.xlsx
│
├── models/
│   └── MultiCity_Thermal_Model_PRO.pkl  # The 141MB trained Random Forest AI
│
├── powerbi/
│   └── Weather Analysis Dashboard.pbix
│
├── src/
│   ├── data_collection.py               # Fetches live API data
│   ├── data_cleaning.py                 # Cleans data & INJECTS AI Predictions
│   ├── sql_storage.py                   # Saves AI-enriched data to SQLite
│   ├── sql_queries.py                   # Analytical queries
│   ├── analysis.py                      
│   ├── excel_report.py
│   └── visualizations.py                # Matplotlib scripts
│
├── visualizations/                      # Generated charts (.png)
├── requirements.txt
└── README.md


## 📍 Cities Analyzed
Karachi, Lahore, Islamabad, Rawalpindi, Peshawar, Quetta, Multan, Astore.

## 💡 Key Skills Demonstrated
* Big Data Handling & API Rate Limit Bypassing
* Machine Learning Model Deployment (Pickle/Scikit-Learn)
* Data Pipeline Automation (ETL)
* SQL Database Design
* Power BI Dashboarding