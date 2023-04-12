import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect("bdd.db")

df = pd.read_sql_query("SELECT * FROM objet_trouve ",conn)

st.dataframe(df)