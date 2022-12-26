import pandas as pd
import plotly.express as px

FILENAME = r"C:\Users\Maxime\PycharmProjects\ProjetE3FIAccidentsMortels\data\usagers-2021.csv"

def get_data(filename):
    return pd.read_csv(filename, sep=";")

#return the number of accidents caused by mans
def get_accidents_homme():
    data = get_data(FILENAME)
    data = data[data["sexe"] == 1]
    return data.value_counts().sum()

def get_accidents_femme():
    data = get_data(FILENAME)
    data = data[data["sexe"] == 2]
    return data.value_counts().sum()

def camembert_accident_par_sexe():
    labels = ["Homme", "Femme"]
    values = [get_accidents_homme(), get_accidents_femme()]
    fig = px.pie(values=values, names=labels, title="Nombre d'accidents par sexe")
    fig.show()

camembert_accident_par_sexe()