# Road-Safety-Analyzer

> 🔗 **Live demo:** https://iambatman07-saferouteanalyzer.hf.space · [HF Space](https://huggingface.co/spaces/IamBatman07/SafeRouteAnalyzer)

An **interactive Streamlit app** to explore road accidents in India, visualize trends and causes, forecast future fatalities/casualties, and plan safer routes using historical accident data, environmental factors, and simulated traffic.

---

## 🧾 Project Description

This project provides an **interactive web app** with multiple tabs for analyzing and predicting road accidents:

- **Data Visualization:** Interactive charts (Plotly: bar, pie, line, area, scatter)  
- **Geospatial Analysis:** Folium maps to display routes and accident hotspots  
- **Machine Learning:** Random Forest Classifier to predict accident severity  
- **Forecasting:** ARIMA-based future accident prediction  
- **Safe Route Planning:** Scenario-based route safety analysis using simulated traffic and weather conditions  

Ideal for **researchers, policymakers, transport planners, and road safety analysts**.

---

## 📂 Project Structure

```
India_Road_Accidents_Analysis/
│
├── app.py
├── data/
│   ├── dataset1.csv
│   ├── dataset2.csv
│   ├── dataset3.csv
│   ├── dataset4.csv
│   ├── dataset5.csv
│   └── dataset6.csv
├── static/
│   └── style.css
├── templates/
│   └── dashboard.html
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📥 Dataset Setup

**Note:** Large datasets (>100MB) are not included.  

1. Create a `data/` folder in the project root.  
2. Place CSV files there: `dataset1.csv` to `dataset6.csv`.  
3. Recommended sources:  
   - [India Open Government Data](https://data.gov.in)  
   - Other verified accident statistics sources  

> For demonstration, you can use a smaller sample of rows.

---

## ⚙️ Installation & Run

```bash
# Clone repository
git clone https://github.com/<your-username>/India_Road_Accidents_Analysis.git
cd India_Road_Accidents_Analysis

# Create virtual environment
python -m venv venv

# Activate environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
```

---

## 📊 Features

- **Dynamic Filters:** Filter by **State, City, or Year** (one filter at a time)  
- **Key Metrics:** Total accidents, fatalities, and casualties  

### Visualizations
- Pie chart: Accident severity distribution  
- Bar charts: Vehicle type, day of week, top causes, time of day  
- Area chart: Monthly accident trends  
- Line chart: Long-term road accident trends  
- Scatter plot: Fatalities vs casualties  
- Interactive Map: Route comparison and accident hotspots using Folium  

- **ML Prediction:** Predict accident severity based on vehicle type, day of week, fatalities, and casualties  

---

## 🧠 Machine Learning Module

- **Model:** Random Forest Classifier  
- **Features:** Vehicle Type, Day of Week, Number of Fatalities, Number of Casualties  
- **Target:** Accident Severity  
- **Usage:** Input values in the sidebar to predict accident severity instantly  

---

## 🚦 Forecasting & Risk Analysis

- **ARIMA Forecasting:** Predict next year’s fatalities and casualties based on historical trends  
- **Scenario-Based Risk Prediction:** Calculate risk scores using:
  - Weather conditions  
  - Terrain type  
  - Traffic density  
  - Visibility  

---

## 🗺️ Safe Route Planner

- Simulates multiple routes between cities  
- Assigns **risk scores** based on:
  - Historical accident data  
  - Weather and month  
  - Simulated traffic  
- Displays **best route** with reasoning and interactive Folium map  

---

## 🌐 Tech Stack

- **Python**  
- **Streamlit**  
- **Pandas**  
- **Plotly**  
- **Folium**  
- **Scikit-learn**  
- **Statsmodels**  
- HTML/CSS templates  