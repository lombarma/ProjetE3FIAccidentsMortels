import pandas as pd
import plotly.express as px

FILENAME = "../data/usagers-2021.csv"


def get_data():
    years = pd.read_csv(FILENAME, sep=";")["an_nais"].value_counts()
    print(years)


get_data()
