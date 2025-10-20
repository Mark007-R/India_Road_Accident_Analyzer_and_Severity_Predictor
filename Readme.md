# 🇮🇳 India Road Accident Analyzer and Severity Predictor

An **interactive Streamlit dashboard** to analyze road accidents in India, visualize accident trends, causes, and hotspots, and predict accident severity using machine learning.

---

## 🧾 Project Description

This project provides an **interactive web application** to explore road accident data at the **state, city, and year levels**.  
It integrates:

- **Data visualization** (Plotly charts, bar/line/area/pie charts)  
- **Geospatial analysis** (Folium maps for accident hotspots)  
- **Machine Learning** (Random Forest Classifier for accident severity prediction)  

The dashboard helps **researchers, policymakers, and road safety analysts** gain insights and identify accident-prone areas.

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
└── README.md


---

## 📥 Dataset Setup

**Note:** Large datasets (over 100 MB) are **not included** in this repo.  

1. Create a folder `data/` inside the project root.  
2. Place your CSV datasets in the folder:


data/
├── dataset1.csv
├── dataset2.csv
├── dataset3.csv
├── dataset4.csv
├── dataset5.csv
└── dataset6.csv

3. Recommended sources for datasets:
- [NYC Motor Vehicle Collisions](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95)  
- [India Open Government Data](https://data.gov.in)  

> Tip: For demo purposes, you can use a **smaller sample CSV** (first few thousand rows).

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/India_Road_Accident_Analyzer_and_Severity_Predictor.git
cd India_Road_Accident_Analyzer_and_Severity_Predictor

2️⃣ Create a Virtual Environment (Optional but Recommended)
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3️⃣ Run the App
streamlit run app.py


Open your browser at http://localhost:8501

📊 Features

Dynamic Filters: Filter by State, City, or Year

Key Metrics: Total accidents, fatalities, and casualties

Visualizations:

Pie chart: Accident severity

Bar charts: Vehicle type, day of week, causes, and time of day

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

Scikit-learn (ML)

HTML/CSS templates for dashboard styling