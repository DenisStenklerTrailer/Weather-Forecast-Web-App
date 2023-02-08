import streamlit as st
import plotly.express as px
import backend

st.title("Weather Forecast for the next days")
place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1, max_value=5, help="Select the number of days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

data = backend.get_data(place, days, option)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (°C)"})
st.plotly_chart(figure)

