import requests
import sqlite3
import bdd
import request_gare
from request_journee import days_list
gares = [
    'Paris Bercy',
    'Paris Gare du Nord',
    'Paris Est',
    'Paris Gare de Lyon',
    'Paris Montparnasse',
    'Paris Saint-Lazare',
    'Paris Austerlitz'
    ]
annees = [annee for annee in range(2019,2023)]

def get_lost_objects(gares, annees):
    results = []
    for gare in gares:
        for annee in annees:
            response = requests.get(f'https://a67b4b4d-cb00-45aa-9970-2c69b46cea8a@ressources.data.sncf.com/api/records/1.0/search/?dataset=objets-trouves-restitution&lang=fr&rows=10000&sort=date&facet=date&facet=gc_obo_gare_origine_r_name&facet=gc_obo_type_c&refine.date={annee}&refine.gc_obo_gare_origine_r_name={gare}')
            results.append(response.json()["records"])
    return results

def get_gare_id_by_name(name : str):

    referencies = {
        "lyon" : 1,
        "montparnasse" : 2,
        "nord" : 3,
        "lazare" : 4,
        "est" : 5,
        "bercy" : 6,
        'austerlitz' : 7,
    }
    for ref in referencies.keys():
        if ref in name.lower():
            return referencies[ref]
    return 404

def get_day_id_by_str(date : str):
    id = list(filter(lambda dic: dic['date'] == date, days_list))
    return id[0]['id']


request_objects_list = get_lost_objects(gares, annees)

objects_liste = []
for items_by_gareyear in request_objects_list:
    for item in items_by_gareyear:
        item = item["fields"]
        objects_liste.append({"gare_id" : get_gare_id_by_name(item['gc_obo_gare_origine_r_name']), "type" : item['gc_obo_type_c'], "date" : get_day_id_by_str(item["date"][:10])})

connexion = sqlite3.connect("bdd.db")
curseur = connexion.cursor()

for objet in objects_liste:
    curseur.execute("""
        INSERT INTO objet_trouve
            VALUES (NULL, ?, ?, ?)
    """, (objet["type"], objet["gare_id"], objet["date"]))
    connexion.commit()
connexion.close()