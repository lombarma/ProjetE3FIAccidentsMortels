import pandas as pd
import plotly.express as px

FILENAME = "data/vehicules-2021.csv"
CATEGORIES = {"Indéterminable": [-1, 0], "Bicyclette": [1], "Voiturette": [3],
              "Véhicules Légers": [7], "Véhicules Utilitaires": [10], "Poids Lourd": [13, 14, 15],
              "Tracteur Routier/Agricole": [16, 17, 21], "Scooter": [2, 30, 32, 34], "Moto": [31, 33],
              "Quad": [35, 36], "Autobus/car": [37, 38], "Train/Tramway": [39, 40], "3 roues motorisé": [41, 42, 43],
              "Engin de déplacement personnel": [50, 60], "Vélo à Assistance Electrique": [80], "Autres": [20, 99]}


def get_data():
    """
    :return: a DataFrame with the categories of vehicles and the number of accidents
    """
    return pd.read_csv(FILENAME, sep=";")["catv"].value_counts()


def dict_catv():
    """
    :return: return a dictionary with the categories of vehicles and the number of accidents
    """
    catv = get_data()
    dict_catv = {}

    for k, v in catv.items():
        for k2, v2 in CATEGORIES.items():
            if k in v2:
                if k2 in dict_catv:
                    dict_catv[k2] += v
                else:
                    dict_catv[k2] = v
    return dict_catv


def scatter_vehicle_categories():
    """
    :return: the scatter plot of the number of accidents by vehicle categories
    """
    data = dict_catv()
    fig = px.scatter(x=data.values(), y=data.keys(), color=data.keys(), size=data.values(),
                     labels={"x": "Nombre d'accidents", "y": "Catégorie de véhicule", "color": "Catégories"},
                     size_max=100, log_x=True, title="Nombre d'accidents par catégorie de véhicule")
    return fig
