# 🇮🇳 India Road Accident Analyzer and Severity Predictor

An **interactive Streamlit dashboard** to analyze road accidents in India, visualize trends, causes, hotspots, and predict accident severity using machine learning.

---

## 🧾 Project Description

This project provides an interactive web app to explore road accident data at **state, city, and year levels**.  
It includes:

- **Data Visualization** (Plotly charts: bar, pie, line, area, scatter)  
- **Geospatial Analysis** (Folium maps for accident hotspots)  
- **Machine Learning** (Random Forest Classifier for accident severity prediction)  

Ideal for researchers, policymakers, and road safety analysts.

---

## 📂 Project Structure

India_Road_Accident_Analyzer_and_Severity_Predictor/
│
├── app.py
├── data/
│ ├── dataset1.csv
│ ├── dataset2.csv
│ ├── dataset3.csv
│ ├── dataset4.csv
│ ├── dataset5.csv
│ └── dataset6.csv
├── static/
│ └── style.css
├── templates/
│ └── dashboard.html
├── .gitignore
├── requirements.txt
└── README.md

yaml
Copy code

---

## 📥 Dataset Setup

**Note:** Large datasets (>100MB) are not included.  

1. Create a `data/` folder in the project root.  
2. Place the CSV files there: `dataset1.csv` to `dataset6.csv`.  
3. Recommended sources:  
   - [NYC Motor Vehicle Collisions](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95)  
   - [India Open Government Data](https://data.gov.in)  

> For demo, you can use a smaller sample of rows.

---

## ⚙️ Installation & Run

```bash
# Clone repository
git clone https://github.com/<your-username>/India_Road_Accident_Analyzer_and_Severity_Predictor.git
cd India_Road_Accident_Analyzer_and_Severity_Predictor

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
Open in browser: http://localhost:8501

📊 Features
Dynamic Filters: Filter by State, City, or Year

Key Metrics: Total accidents, fatalities, casualties

Visualizations
Pie chart: Accident severity

Bar charts: Vehicle type, day of week, causes, time of day

Area chart: Monthly trends

Line chart: Long-term trends

Scatter plot: Fatalities vs casualties

Interactive Map: Accident hotspots with Folium

ML Prediction: Predict accident severity using vehicle type, day of week, fatalities, and casualties

🧠 Machine Learning Module
Model: Random Forest Classifier

Features: Vehicle Type, Day of Week, Number of Fatalities, Number of Casualties

Target: Accident Severity

Usage: Enter values in the sidebar and predict severity instantly

🌐 Tech Stack
Python, Streamlit, Pandas, Plotly, Folium

Scikit-learn

HTML/CSS templates
