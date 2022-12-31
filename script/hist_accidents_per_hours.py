import pandas as pd
import plotly.express as px

FILENAME = "data/carcteristiques-2021.csv"


def get_data():
    """
    :return: a list of hours
    """
    hours = pd.read_csv(FILENAME, sep=";")["hrmn"]
    hours = hours.apply(lambda x: int(str(x)[:2]))
    return hours


def histogram_accidents_per_hours():
    """
    :return: a histogram showing the number of accidents per hours
    """
    hours = get_data()
    fig = px.histogram(hours, x=hours, nbins=24, title="Nombre d'accidents par heure")
    fig.update_traces(opacity=0.8)
    fig.update_layout(xaxis_title="Heure", yaxis_title="Nombre d'accidents")
    return fig
