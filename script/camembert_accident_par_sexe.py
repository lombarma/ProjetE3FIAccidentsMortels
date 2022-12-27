import pandas as pd
import plotly.express as px

FILENAME = "data/usagers-2021.csv"


def get_data(filename):
    """
    :param filename: the filename of the csv file
    :return: DataFrame
    """
    return pd.read_csv(filename, sep=";")


def get_accidents_men():
    """
    :return: the sum of accidents where man was involved
    """
    data = get_data(FILENAME)
    data = data[data["sexe"] == 1]
    return data.value_counts().sum()


def get_accidents_women():
    """
    :return: the sum of accidents where woman was involved
    """
    data = get_data(FILENAME)
    data = data[data["sexe"] == 2]
    return data.value_counts().sum()


def get_accidents_unknown():
    """
    :return: the sum of accidents where unknown gender was involved
    """
    data = get_data(FILENAME)
    data = data[(data["sexe"] != 1) & (data["sexe"] != 2)]
    return data.value_counts().sum()


def pie_chart_accident_by_sex():
    """
    :return: a pie chart showing the number of accidents
    """
    labels = ["Homme", "Femme", "Inconnu"]
    values = [get_accidents_men(), get_accidents_women(), get_accidents_unknown()]
    fig = px.pie(values=values, names=labels, title="Nombre d'accidents par sexe")
    #fig.show()
    return fig


pie_chart_accident_by_sex()
