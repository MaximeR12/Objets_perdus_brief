import sqlite3
import requests

connexion = sqlite3.connect("bdd.db")
curseur = connexion.cursor()

response = requests.get("https://archive-api.open-meteo.com/v1/archive?latitude=48.85&longitude=2.35&start_date=2019-01-01&end_date=2022-12-31&daily=temperature_2m_mean&timezone=Europe%2FBerlin")

date_list = response.json()["daily"]["time"]
temperature_list = response.json()["daily"]["temperature_2m_mean"]
