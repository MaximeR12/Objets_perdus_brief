import sqlite3
import requests

connexion = sqlite3.connect("bdd.db")
curseur = connexion.cursor()

liste_gare = ["Paris Gare de Lyon", "Paris Montparnasse", "Paris Gare du Nord", "Paris Saint-Lazare", "Paris Est", "Paris Bercy Bourgogne - Pays d%27Auvergne", "Paris Austerlitz"]

for gare in liste_gare:
    response = requests.get(f"https://ressources.data.sncf.com/api/records/1.0/search/?dataset=frequentation-gares&q=&facet=nom_gare&refine.nom_gare={gare}")
    frequentation_2019 = response.json()['records'][0]['fields']['total_voyageurs_2019']
    frequentation_2020 = response.json()['records'][0]['fields']['total_voyageurs_2020']
    frequentation_2021 = response.json()['records'][0]['fields']['total_voyageurs_2021']
    
    curseur.execute("""
                        INSERT INTO gare
                            VALUES (NULL, ?, ?, ?, ?)
                        """, (gare, frequentation_2019, frequentation_2020, frequentation_2021))
    
    connexion.commit()

connexion.close()