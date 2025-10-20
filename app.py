import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="India Road Accidents Analysis", layout="wide")

@st.cache_data
def load_data():
    ds1 = pd.read_csv("data/dataset1.csv")
    ds2 = pd.read_csv("data/dataset2.csv")
    ds3 = pd.read_csv("data/dataset3.csv")
    ds4 = pd.read_csv("data/dataset4.csv")
    ds5 = pd.read_csv("data/dataset5.csv")
    ds6 = pd.read_csv("data/dataset6.csv")
    return ds1, ds2, ds3, ds4, ds5, ds6

ds1, ds2, ds3, ds4, ds5, ds6 = load_data()

st.sidebar.title("Filters (Select only ONE)")

states = ["All"] + sorted(ds1['State Name'].dropna().unique().tolist())
cities = ["All"] + sorted(ds1['City Name'].dropna().unique().tolist())
years = ["All"] + sorted(ds1['Year'].dropna().unique().tolist())

if "active_filter" not in st.session_state:
    st.session_state.active_filter = None

selected_state = st.sidebar.selectbox("Select State", options=states)
if selected_state != "All":
    st.session_state.active_filter = "state"
else:
    if st.session_state.active_filter == "state":
        st.session_state.active_filter = None

selected_city = st.sidebar.selectbox(
    "Select City",
    options=cities,
    disabled=(st.session_state.active_filter not in [None, "city"])
)
if selected_city != "All":
    st.session_state.active_filter = "city"
else:
    if st.session_state.active_filter == "city":
        st.session_state.active_filter = None

selected_year = st.sidebar.selectbox(
    "Select Year",
    options=years,
    disabled=(st.session_state.active_filter not in [None, "year"])
)
if selected_year != "All":
    st.session_state.active_filter = "year"
else:
    if st.session_state.active_filter == "year":
        st.session_state.active_filter = None

if st.session_state.active_filter == "state":
    selected_city, selected_year = "All", "All"
elif st.session_state.active_filter == "city":
    selected_state, selected_year = "All", "All"
elif st.session_state.active_filter == "year":
    selected_state, selected_city = "All", "All"

def filter_data(df):
    df_filtered = df.copy()
    if selected_state != "All":
        df_filtered = df_filtered[df_filtered['State Name'] == selected_state]
    elif selected_city != "All":
        df_filtered = df_filtered[df_filtered['City Name'] == selected_city]
    elif selected_year != "All":
        df_filtered = df_filtered[df_filtered['Year'] == selected_year]
    return df_filtered

ds1_filtered = filter_data(ds1)

st.title("📊 India Road Accidents Interactive Dashboard")

col1, col2, col3 = st.columns(3)
col1.metric("🚗 Total Accidents", len(ds1_filtered))
col2.metric("☠️ Total Fatalities", int(ds1_filtered['Number of Fatalities'].sum()))
col3.metric("💥 Total Casualties", int(ds1_filtered['Number of Casualties'].sum()))

st.markdown("---")

chart_gradients = ['Greens', 'Blues']
color_idx = 0

if not ds1_filtered.empty:
    severity_counts = ds1_filtered['Accident Severity'].value_counts()
    fig_severity = px.pie(
        values=severity_counts.values,
        names=severity_counts.index,
        title="Accident Severity Distribution",
        color_discrete_sequence=[px.colors.sequential.Greens[i*2] for i in range(len(severity_counts))]
        if color_idx == 0 else [px.colors.sequential.Blues[i*2] for i in range(len(severity_counts))]
    )
    fig_severity.update_traces(textinfo='percent+label', pull=[0.05]*len(severity_counts))
    st.plotly_chart(fig_severity, use_container_width=True)
    color_idx = 1 - color_idx 

if not ds1_filtered.empty:
    vehicle_counts = ds1_filtered['Vehicle Type Involved'].value_counts().reset_index()
    vehicle_counts.columns = ['Vehicle Type', 'Count']
    fig_vehicle = px.bar(
        vehicle_counts,
        x='Vehicle Type',
        y='Count',
        color='Count',
        color_continuous_scale=chart_gradients[color_idx],
        title="🚘 Accidents by Vehicle Type",
        text='Count'
    )
    fig_vehicle.update_traces(texttemplate='%{text}', textposition='outside')
    st.plotly_chart(fig_vehicle, use_container_width=True)
    color_idx = 1 - color_idx

if not ds1_filtered.empty:
    day_counts = ds1_filtered['Day of Week'].value_counts().reset_index()
    day_counts.columns = ['Day of Week', 'Count']
    fig_day = px.bar(
        day_counts,
        x='Day of Week',
        y='Count',
        color='Count',
        color_continuous_scale=chart_gradients[color_idx],
        title="📅 Accidents by Day of the Week",
        text='Count'
    )
    fig_day.update_traces(texttemplate='%{text}', textposition='outside')
    st.plotly_chart(fig_day, use_container_width=True)
    color_idx = 1 - color_idx

if selected_state != "All":
    ds4_filtered = ds4[ds4['STATE/UT'] == selected_state]
    if selected_year != "All":
        ds4_filtered = ds4_filtered[ds4_filtered['YEAR'] == int(selected_year)]
    if not ds4_filtered.empty:
        months = ['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
        monthly_accidents = ds4_filtered[months].iloc[0]
        fig_month = px.area(
            x=months,
            y=monthly_accidents.values,
            title=f"Monthly Accidents Trend - {selected_state}",
            labels={'x':'Month','y':'Accidents'},
            color_discrete_sequence=['#00CC96']  # green
        )
        st.plotly_chart(fig_month, use_container_width=True)
        color_idx = 1 - color_idx

if selected_state != "All":
    ds5_filtered = ds5[ds5['STATE/UT'] == selected_state]
    if selected_year != "All":
        ds5_filtered = ds5_filtered[ds5_filtered['YEAR'] == int(selected_year)]
    if not ds5_filtered.empty:
        time_cols = ds5.columns[2:-1]
        time_counts = ds5_filtered[time_cols].iloc[0]
        fig_time = px.bar(
            x=time_cols,
            y=time_counts.values,
            color=time_counts.values,
            color_continuous_scale=chart_gradients[color_idx],
            title=f"Accidents by Time of Day - {selected_state}"
        )
        st.plotly_chart(fig_time, use_container_width=True)
        color_idx = 1 - color_idx

st.subheader("🗺️ Accident Hotspots Map")
if 'Latitude' in ds1_filtered.columns and 'Longitude' in ds1_filtered.columns:
    ds_map = ds1_filtered.dropna(subset=['Latitude','Longitude'])
    m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)
    for _, row in ds_map.iterrows():
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=6,
            popup=f"<b>{row['City Name']}</b><br>Severity: {row['Accident Severity']}",
            color='red' if row['Accident Severity']=="Serious" else 'orange',
            fill=True
        ).add_to(m)
    st_folium(m, width=700)
else:
    st.info("No latitude/longitude available for map plotting.")

st.subheader("🚦 Top Accident Causes in Million+ Cities")
if {'Cause category', 'Count'}.issubset(ds2.columns):
    ds2_filtered = ds2.copy()
    if selected_city != "All":
        ds2_filtered = ds2_filtered[ds2_filtered['Million Plus Cities']==selected_city]
    if not ds2_filtered.empty:
        cause_counts = ds2_filtered.groupby('Cause category')['Count'].sum().sort_values(ascending=False)
        cause_df = pd.DataFrame({'Cause': cause_counts.index, 'Count': cause_counts.values})
        fig_cause = px.bar(
            cause_df,
            x='Cause', y='Count',
            color='Count',
            color_continuous_scale=chart_gradients[color_idx],
            title="Top Accident Causes"
        )
        st.plotly_chart(fig_cause, use_container_width=True)
        color_idx = 1 - color_idx

st.subheader("📈 Long-term Accident Trends in India")
fig_trend = px.line(
    ds6,
    x='Years',
    y='Total Number of Road Accidents (in numbers)',
    markers=True,
    color_discrete_sequence=['#1f77b4'],  # blue
    title="Total Road Accidents Over Years"
)
fig_trend.update_layout(xaxis_title="Year", yaxis_title="Accidents", hovermode="x unified")
st.plotly_chart(fig_trend, use_container_width=True)
color_idx = 1 - color_idx

if 'Number of Fatalities' in ds1_filtered.columns:
    st.subheader("⚠️ Severity vs Fatalities Scatter Plot")
    fig_scatter = px.scatter(
        ds1_filtered,
        x='Number of Fatalities',
        y='Number of Casualties',
        color='Number of Fatalities',           # numeric column
        color_continuous_scale=['#1f77b4','#00CC96'],  # blue → green gradient
        hover_data=['State Name','City Name'],
        title="Fatalities vs Casualties (Blue → Green Gradient)"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown("---")
st.header("🤖 Accident Severity Prediction (ML Feature)")

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

if 'Accident Severity' in ds1.columns:
    ml_df = ds1[['Vehicle Type Involved', 'Day of Week', 'Number of Fatalities', 'Number of Casualties', 'Accident Severity']].dropna()

    le_vehicle = LabelEncoder()
    le_day = LabelEncoder()
    le_severity = LabelEncoder()

    ml_df['Vehicle Type Involved'] = le_vehicle.fit_transform(ml_df['Vehicle Type Involved'])
    ml_df['Day of Week'] = le_day.fit_transform(ml_df['Day of Week'])
    ml_df['Accident Severity'] = le_severity.fit_transform(ml_df['Accident Severity'])

    X = ml_df[['Vehicle Type Involved', 'Day of Week', 'Number of Fatalities', 'Number of Casualties']]
    y = ml_df['Accident Severity']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    st.subheader("Enter Accident Details to Predict Severity")

    col1, col2 = st.columns(2)
    with col1:
        vehicle_input = st.selectbox("Vehicle Type", options=le_vehicle.classes_)
        fatalities_input = st.number_input("Number of Fatalities", min_value=0, max_value=50, value=0)
    with col2:
        day_input = st.selectbox("Day of Week", options=le_day.classes_)
        casualties_input = st.number_input("Number of Casualties", min_value=0, max_value=100, value=0)

    if st.button("Predict Severity 🚦"):
        input_df = pd.DataFrame({
            'Vehicle Type Involved': [le_vehicle.transform([vehicle_input])[0]],
            'Day of Week': [le_day.transform([day_input])[0]],
            'Number of Fatalities': [fatalities_input],
            'Number of Casualties': [casualties_input]
        })

        prediction = model.predict(input_df)
        predicted_label = le_severity.inverse_transform(prediction)[0]

        st.success(f"✅ Predicted Severity: **{predicted_label}**")

else:
    st.warning("ML Prediction cannot be run — 'Accident Severity' column missing in dataset.")
