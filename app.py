import streamlit as st
import numpy as np
import folium
import pandas as pd
from streamlit_folium import st_folium

def get_color(risk_score):
    return "green" if risk_score <= 25 else "orange" if risk_score > 25 and risk_score <= 50 else "red" if risk_score > 50 and risk_score <= 75 else "darkred"


st.title("Global AQI Risk")

df = pd.read_csv(r"data/map_df.csv")
world_risk_map = folium.Map(location=[20,0],zoom_start=2,tiles="CartoDB positron")

for _,row in df.iterrows():
    folium.CircleMarker(
        location = [row["latitude"],row["longitude"]],
        radius = 10,
        color = get_color(row["risk_score"]),
        fill = True,
        fill_color = get_color(row["risk_score"]),
        fill_opacity=0.6,
        popup=f"{row['City/Town']} | Risk Score: {round(row['risk_score'], 2)} | PM2.5: {row['PM2.5']}",
        tool_tip="Click me"
    ).add_to(world_risk_map)

st_folium(world_risk_map,width=1200)
col1,col2,col3,col4 = st.columns(4)
with col1:
    st.metric(label="Total Cities Monitored", value=df["City/Town"].count())
with col2:
    st.metric(label="Number of Very High Risk cities",value=df[df["risk_category"] == "Very High Risk"].shape[0])
with col3:
    st.metric(label="Average global PM2.5",value=round(df["PM2.5"].mean(),1))
with col4:
    st.metric(label="Most polluted City",value=df.loc[df["risk_score"].idxmax(), "City/Town"])