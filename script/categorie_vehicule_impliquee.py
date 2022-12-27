import pandas as pd
import plotly.express as px

FILENAME = "data/vehicules-2021.csv"
CATEGORIES = {"Indéterminable": [-1, 0], "Bicyclette": [1], "Voiturette": [3],
              "Véhicules Légers": [7], "Véhicules Utilitaires": [10], "Poids Lourd": [13, 14, 15],
              "Tracteur Routier/Agricole": [16, 17, 21], "Scooter": [2, 30, 32, 34], "Moto": [31, 33],
              "Quad": [35, 36], "Autobus/car": [37, 38], "Train/Tramway": [39, 40], "3 roues motorisé": [41, 42, 43],
              "Engin de déplacement personnel": [50, 60], "Vélo à Assistance Electrique": [80], "Autres": [20, 99]}


def get_data():
    data = pd.read_csv(FILENAME, sep=";")
    catv = data["catv"].value_counts()
    return catv


def chart_vehicle_categories():
    catv = get_data()
    dict_catv = {}

    for k, v in catv.items():
        for k2, v2 in CATEGORIES.items():
            if k in v2:
                if k2 in dict_catv:
                    dict_catv[k2] += v
                else:
                    dict_catv[k2] = v

    fig = px.scatter(x=dict_catv.values(), y=dict_catv.keys(), color=dict_catv.keys(), size=dict_catv.values(), size_max=100,
                     title="Graphique montrant le nombre d'accidents en fonction de la catégorie du véhicule impliqué")
    fig.update_layout(xaxis_title="Nombre d'accidents", yaxis_title="Catégorie du véhicule impliqué")
    return fig


