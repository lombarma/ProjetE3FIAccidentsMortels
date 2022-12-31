import branca
import folium
import pandas as pd

FILENAME = "data/carcteristiques-2021.csv"


def get_data():
    data = pd.read_csv(FILENAME, sep=";")
    dep = data["dep"].value_counts()
    for k, v in dep.items():
        if v < 500:
            dep = dep.drop(k)

    coordinates = {row[1]["dep"]: [float(row[1]["lat"].strip().replace(",", ".")), float(row[1]["long"].strip().replace(",", "."))] for row in data.iterrows()}
    return dep, coordinates


def accident_distribution_map():
    dep, coordinates = get_data()
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
