import streamlit as st
import plotly.express as px
import pandas as pd

options = ("happiness","gdp","generosity"
,"country", "social_support","life_expectancy"
,"freedom_to_make_life_choices", "corruption"
)

st.title("In Search for Happiness")
x_axis = st.selectbox("Select the data for the X-axis: ", options=options)
y_axis = st.selectbox("Select the data for the Y-axis: ", options=options)

st.subheader(f"{x_axis} and {y_axis}")

df = pd.read_csv("happy.csv")

x_data = df[x_axis]

y_data = df[y_axis]

country = df['country']

figure = px.scatter(x=x_data, y=y_data, 
                labels={"x": x_axis, "y": y_axis}, hover_data={"country": country})

st.plotly_chart(figure)