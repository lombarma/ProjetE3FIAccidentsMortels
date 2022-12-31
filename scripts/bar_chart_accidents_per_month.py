import pandas as pd
import plotly.express as px

FILENAME = "data/carcteristiques-2021.csv"

dict_month = {1: "Janvier", 2: "Février", 3: "Mars", 4: "Avril", 5: "Mai", 6: "Juin", 7: "Juillet", 8: "Août",
              9: "Septembre", 10: "Octobre", 11: "Novembre", 12: "Décembre"}


def get_data():
    """
    :return: a DataFrame with the number of accidents by month
    """
    return pd.read_csv(FILENAME, sep=";")["mois"].value_counts()


def bar_char_accidents_by_month():
    """
    :return: the bar chart of the number of accidents by month
    """
    data = get_data()
    fig = px.bar(data, x=data.index, y=data.values, color=data.index, labels={"x": "Mois", "y": "Nombre d'accidents"}, title="Nombre d'accidents par mois")
    fig.update_layout(xaxis_title="Mois", yaxis_title="Nombre d'accidents", title="Nombre d'accidents par mois")
    fig.update_xaxes(ticktext=list(dict_month.values()), tickvals=list(dict_month.keys()))
    return fig
