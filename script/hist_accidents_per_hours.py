import pandas as pd
import plotly.express as px

FILENAME = "data/carcteristiques-2021.csv"


def histogram_accidents_per_hours():
    hours = pd.read_csv(FILENAME, sep=";")["hrmn"]
    hours = hours.apply(lambda x: int(str(x)[:2]))
    fig = px.histogram(hours, x=hours, nbins=24, title="Nombre d'accidents par heure")
    fig.update_traces(opacity=0.75)
    fig.update_layout(xaxis_title="Heure", yaxis_title="Nombre d'accidents")
    return fig
