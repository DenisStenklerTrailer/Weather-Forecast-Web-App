import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("happy.csv")

st.title("In Search for Happiness")

x = st.selectbox("Select data for the X-axis", ("GDP", "Happiness", "Generosity", "Corruption", "Freedom to make life choices",
                 "Social support", "Life expectancy"), key="x_plot")
y = st.selectbox("Select data for the Y-axis", ("GDP", "Happiness", "Generosity", "Corruption", "Freedom to make life choices",
                 "Social support", "Life expectancy"), key="y_plot")

st.subheader(f"{x} and {y}")
figure = px.scatter(x=df[(x.lower()).replace(" ", "_")], y=df[(y.lower()).replace(" ", "_")], labels={"x": x, "y": y})
st.plotly_chart(figure)


