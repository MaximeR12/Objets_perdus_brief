import sqlite3

connexion = sqlite3.connect("bdd.db")
curseur = connexion.cursor()

curseur.execute("""
                CREATE TABLE IF NOT EXISTS gare (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT NOT NULL,
                    frequentation_2019 INTEGER NOT NULL,
                    frequentation_2020 INTEGER NOT NULL,
                    frequentation_2021 INTEGER NOT NULL
                )
                """)

connexion.commit()

curseur.execute("""
                CREATE TABLE IF NOT EXISTS journee (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date DATE NOT NULL,
                    temperature INTEGER NOT NULL
                )
                """)

connexion.commit()

curseur.execute("""
                CREATE TABLE IF NOT EXISTS objet_trouve (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    type TEXT NOT NULL,
                    gare_id INTEGER,
                    journee_id INTEGER,
                    FOREIGN KEY(gare_id) REFERENCES gare(id),
                    FOREIGN KEY(journee_id) REFERENCES journee(id)
                )
                """)

connexion.commit()

connexion.close()