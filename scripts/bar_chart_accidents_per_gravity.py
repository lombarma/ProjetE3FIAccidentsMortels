import pandas as pd
import plotly.express as px

FILENAME = "data/usagers-2021.csv"


def get_data():
    """
    Returns the data from the CSV file
    :return: data
    """
    data = pd.read_csv(FILENAME, sep=";")
    return data


def get_accidents_by_gravity():
    """
    :return: the number of accidents by gravity
    """
    data = get_data()
    data = data["grav"].value_counts()
    for i in data.index:
        if i < 1:
            data = data.drop(i)
    return data


def bar_chart_accident_by_gravity():
    """
    :return: the bar chart of the number of accidents by gravity
    """
    data = get_accidents_by_gravity()
    labels = ["Indemne", "Blessé léger", "Blessé hospitalisé", "Tué"]
    fig = px.bar(data, x=labels, y=data.values, color=data.index, text=data.values, range_y=[0, data.max()])
    fig.update_layout(xaxis_title="Gravité", yaxis_title="Nombre d'accidents", title="Nombre d'accidents par gravité")
    return fig
