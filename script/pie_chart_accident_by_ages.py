import pandas as pd
import plotly.express as px

FILENAME = "data/usagers-2021.csv"


def get_data():
    """
    :return: a DataFrame with the number of accidents by year
    """
    years = pd.read_csv(FILENAME, sep=";")["an_nais"].value_counts()
    return years


def get_age_range(year):
    """
    :param year: the year of the accident
    :return: the age range of the person who was involved in the accident
    """
    age = 2022 - year
    if age < 15:
        age_range = "moins de 15 ans"
    elif age < 20:
        age_range = "15-19 ans"
    elif age < 25:
        age_range = "20-24 ans"
    elif age < 30:
        age_range = "25-29 ans"
    elif age < 35:
        age_range = "30-34 ans"
    elif age < 40:
        age_range = "35-39 ans"
    elif age < 45:
        age_range = "40-44 ans"
    elif age < 50:
        age_range = "45-49 ans"
    elif age < 55:
        age_range = "50-54 ans"
    elif age < 60:
        age_range = "55-59 ans"
    elif age < 65:
        age_range = "60-64 ans"
    elif age < 70:
        age_range = "65-69 ans"
    elif age < 75:
        age_range = "70-74 ans"
    else:
        age_range = "75 ans et plus"
    return age_range


def age_groups():
    """
    :return: a dict of the number of accidents by age group
    """
    years = get_data()
    age_groups = {}

    for year in years.index:
        age_range = get_age_range(year)

        if age_range in age_groups:
            age_groups[age_range] += years[year]
        else:
            age_groups[age_range] = years[year]

    return age_groups


def pie_chart_accident_by_ages():
    """
    :return: a pie chart showing the number of accidents by age
    """
    age_grp = age_groups()
    fig = px.pie(values=age_grp.values(), names=age_grp.keys(), title="Nombre d'accidents par tranche d'âge")
    return fig
