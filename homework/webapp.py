import streamlit as st
import plotly.express as px
import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

cursor.execute("SELECT time FROM temperature")
date = cursor.fetchall()
date = [item[0] for item in date]

cursor.execute("SELECT temperature FROM temperature")
temp = cursor.fetchall()
temp = [item[0] for item in temp]

figure = px.line(x=date, y=temp,
                 labels={"x": "Date", "y": "Temp(C)"})
st.plotly_chart(figure)