import folium
import pandas as pd

FILENAME = "../data/carcteristiques-2021.csv"


def get_data():
    data = pd.read_csv(FILENAME, sep=";")
    dep = data["dep"].value_counts()

    coordinates = {row[1]["dep"]: (float(row[1]["lat"].strip().replace(",", ".")), float(row[1]["long"].strip().replace(",", "."))) for row in data.iterrows()}
    return dep, coordinates


def get_map():
    dep, coordinates = get_data()
    map = folium.Map(location=[46.52863469527167, 2.43896484375], zoom_start=6)
    for i in dep.index:
        folium.CircleMarker(
            location=coordinates[i],
            radius=dep[i] / 100,
            popup=f"{i} - {dep[i]} accidents",
            color='crimson',
            fill=True,
            fill_color='crimson'
        ).add_to(map)
    #return map
    map.save(outfile="map4.html")


#get_data()
get_map()


"""import folium
import pandas as pd

# Chargez le fichier CSV en mémoire en utilisant Pandas
df = pd.read_csv("../data/carcteristiques-2021.csv", sep=";")

column_lat = df["lat"]
column_long = df["long"]

column_lat = column_lat.str.replace(",", ".")
column_long = column_long.str.replace(",", ".")

df["lat"] = column_lat
df["long"] = column_long

# Créez une base de carte avec une latitude et une longitude centrales
m = folium.Map(location=[48.85, 2.35], zoom_start=6)

# Ajoutez chaque point de données à la carte
for index, row in df.iterrows():
    folium.CircleMarker(location=(float(row['lat']), float(row['long'])), radius=1, color='#ff0000').add_to(m)

# Affichez la carte
m.save(outfile="map3.html")"""
#########################################
"""import folium

# Créez une base de carte avec une latitude et une longitude centrales
m = folium.Map(location=[46.52863469527167, 2.43896484375], zoom_start=6)

# Ajoutez les limites des départements de GeoJSON à la carte
folium.GeoJson(
    # Vos données de GeoJSON
    '../data/departements.geojson',
    style_function=lambda feature: {
        'fillColor': '#ffffff',
        'color': '#0000ff',
        'weight': 2,
        'dashArray': '5, 5'
    }
).add_to(m)

# Affichez la carte
m.save(outfile="map2.html")"""

