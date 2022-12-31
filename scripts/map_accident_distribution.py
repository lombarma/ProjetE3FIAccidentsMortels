import branca
import folium
import pandas as pd

FILENAME = "data/carcteristiques-2021.csv"


def get_data():
    """
    :return: data extracted from the csv file
    """
    return pd.read_csv(FILENAME, sep=";")


def number_accidents_by_dep():
    """
    :return: a dict of the number of accidents by department
    """
    dep = get_data()["dep"].value_counts()
    for k, v in dep.items():
        if v < 500:
            dep = dep.drop(k)

    return dep


def get_dep_coordinates():
    """
    :return: a dict of coordinates of each the department
    """
    data = get_data()
    coordinates = {row[1]["dep"]: [float(row[1]["lat"].replace(",", ".")), float(row[1]["long"].replace(",", "."))] for row in data.iterrows()}
    return coordinates


def accident_distribution_map():
    """
    :return: a map showing the number of accidents by department
    """
    dep, coordinates = number_accidents_by_dep(), get_dep_coordinates()
    map = folium.Map(location=[46.539758, 2.430331], zoom_start=7)

    cm = branca.colormap.LinearColormap(['blue', 'red'], vmin=min(dep), vmax=max(dep)/3)
    map.add_child(cm)

    for i in dep.index:
        folium.CircleMarker(
            location=coordinates[i],
            radius=dep[i] / 100,
            popup=f"{i} - {dep[i]} accidents",
            color=cm(dep[i]),
            fill=True,
            fill_color=cm(dep[i]),
            fill_opacity=0.2
        ).add_to(map)

    return map
