import pandas as pd
import plotly.express as px

FILENAME = "data/carcteristiques-2021.csv"

dictionnaire_mois = {1: "Janvier", 2: "Février", 3: "Mars", 4: "Avril", 5: "Mai", 6: "Juin", 7: "Juillet", 8: "Août", 9: "Septembre", 10: "Octobre", 11: "Novembre", 12: "Décembre"}


def get_data():
    """
    return the data from the csv file
    :return: DataFrame
    """
    return pd.read_csv(FILENAME, sep=";")


def get_accidents_by_month():
    """
    :return: the number of accidents by month
    """
    data = get_data()
    data = data["mois"].value_counts()
    return data


def bar_char_accidents_by_month():
    """
    :return: the bar chart of the number of accidents by month
    """
    data = get_accidents_by_month()
    fig = px.bar(data, x=data.index, y=data.values, color=data.index, labels={"x": "Mois", "y": "Nombre d'accidents"}, title="Nombre d'accidents par mois")
    fig.update_layout(xaxis_title="Mois", yaxis_title="Nombre d'accidents", title="Nombre d'accidents par mois")
    fig.update_xaxes(ticktext=list(dictionnaire_mois.values()), tickvals=list(dictionnaire_mois.keys()))
    return fig
