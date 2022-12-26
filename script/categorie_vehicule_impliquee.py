import pandas as pd
import plotly.express as px

FILENAME = "../data/vehicules-2021.csv"
CATEGORIES = {-1: "Inconnu", 0: "Indéterminable", 1: "Bicyclette", 2: "Cyclomoteur < 50 cm3", 3: "Voiturette", 7: "Véhicules Légers", 10: "Véhicules Utilitaires 1.5 à 3.5T",
              13: "Poids Lourd 3.5 à 7.5T", 14: "Poids Lourd > 7.5T", 15: "Poids Lourd > 3.5T + remorque", 17: "Tracteur routier + semi-remorque", 30: "Scooter < 50 cm3", 31: "Motocyclette 50 à 125 cm3",
              32: "Scooter 50 à 125 cm3", 33: "Motocyclette > 125 cm3", 34: "Scooter < 125 cm3", 50: "Engin de déplacement personnel motorisé"}

CATEGORIES = {"Inconnue": [1], }
""" 
7     57101
 33     7510
 10     6745
 1      5618
 2      3822
 30     3380
 32     2221
 31     1685
 50     1510
 15      970
 34      899
 14      734
 17      641
 37      621
 43      612
 80      534
 3       523
 99      438
 13      387
 21      265
 60      237
 0       219
 36      179
 40      133
 38      123
 20       95
 39       41
 16       36
 35       18
 41       11
-1         4
 42        3
 """


def get_data():
    data = pd.read_csv(FILENAME, sep=";")
    catv = data["catv"].value_counts()

    """for k, v in catv.iteritems():
        if v < 900:
            catv = catv.drop(k, axis=0)"""

    return catv


def pie_chart_vehicle_categories():
    catv = get_data()
    dict_catv = {}

    for k, v in catv.iteritems():
        dict_catv[CATEGORIES[k]] = v

    fig = px.scatter(x=dict_catv.keys(), y=dict_catv.values(), title="Camembert des catégories de véhicules les "
                                                                          "plus impliquées dans les accidents")

    fig.show()


#pie_chart_vehicle_categories()
print(get_data())
