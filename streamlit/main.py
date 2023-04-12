import pandas as pd
import sqlite3
import plotly.express as px
import streamlit as st


conn = sqlite3.connect("bdd.db")
df = pd.read_sql("SELECT * FROM objet_trouve", conn)

df['jour'] = pd.to_datetime(df['jour'])

df['semaine'] = df["jour"].dt.isocalendar().week

df_by = df.groupby(by=['type', 'semaine']).count().reset_index()

fig = px.histogram(df_by, x="semaine", y='id', nbins=53, color="type")
fig.update_layout(bargap=0.1)
st.write(fig)