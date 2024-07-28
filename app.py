import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Initialize sample data
@st.cache
def load_weather_data():
    # Sample historical weather data
    data = {
        'Date': pd.date_range(start='2024-01-01', periods=30, freq='D'),
        'Temperature': np.random.uniform(low=0, high=35, size=30),  # Temperature in Celsius
        'Precipitation': np.random.uniform(low=0, high=10, size=30)  # Precipitation in mm
    }
    return pd.DataFrame(data)

weather_data = load_weather_data()

# App title
st.title('Weather Dashboard')

# Current weather conditions (static for this example)
st.subheader('Current Weather Conditions')
st.write("Location: Example City")
st.write("Temperature: 25°C")
st.write("Precipitation: 2 mm")
st.write("Condition: Partly Cloudy")

# Forecast (static for this example)
st.subheader('Weather Forecast')
st.write("Forecast for the next 7 days:")
forecast_data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Temperature': np.random.uniform(low=15, high=30, size=7),
    'Precipitation': np.random.uniform(low=0, high=5, size=7)
}
forecast_df = pd.DataFrame(forecast_data)
st.dataframe(forecast_df)

# Historical data visualization
st.subheader('Historical Weather Data')

# Line chart for temperature trends
st.write("Temperature Trends Over the Last Month")
fig, ax = plt.subplots()
ax.plot(weather_data['Date'], weather_data['Temperature'], marker='o', linestyle='-', color='b')
ax.set_title('Temperature Trend')
ax.set_xlabel('Date')
ax.set_ylabel('Temperature (°C)')
st.pyplot(fig)

# Bar chart for precipitation levels
st.write("Precipitation Levels Over the Last Month")
fig, ax = plt.subplots()
ax.bar(weather_data['Date'], weather_data['Precipitation'], color='blue')
ax.set_title('Precipitation Levels')
ax.set_xlabel('Date')
ax.set_ylabel('Precipitation (mm)')
st.pyplot(fig)

# Radar chart for weather comparisons
st.write("Weather Comparisons")

def radar_chart(data, labels):
    # Ensure data is a list or array-like
    if isinstance(data, pd.Series):
        values = data.values
    else:
        values = np.array(data)
    
    # Ensure the data is in the correct format
    if len(values) != len(labels):
        raise ValueError("Length of data and labels must match.")

    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    values = np.concatenate((values, [values[0]]))  # Close the circle
    angles += angles[:1]  # Complete the loop

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='blue', alpha=0.25)
    ax.plot(angles, values, color='blue', linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_title('Weather Metrics Comparison')

    return fig

# Sample data for radar chart
labels = ['Temperature', 'Precipitation', 'Humidity', 'Wind Speed']
values = [20, 3, 60, 5]  # Example values
fig = radar_chart(values, labels)
st.pyplot(fig)
