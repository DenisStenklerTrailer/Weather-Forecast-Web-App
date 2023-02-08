import streamlit as st
import plotly.express as px
import backend

st.title("Weather Forecast for the next days")
place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1, max_value=5, help="Select the number of days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

# Get the temperature/sky data
filtered_content = []

if place: #We need to first provide a place
    filtered_content = backend.get_data(place, days, option)

    #Create a temperature plot
    if option == "Temperature":
        temperatures = [temp['main']['temp'] for temp in filtered_content]
        date = [date["dt_txt"] for date in filtered_content]
        figure = px.line(x=date, y=temperatures, labels={"x": "Date", "y": "Temperature (°C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png", "Snow": "images/snow.png"}
        sky_conditions = [sky['weather'][0]['main'] for sky in filtered_content]
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, width=150)


