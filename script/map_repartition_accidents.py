"""import folium
import pandas as pd

# Chargez le fichier CSV en mémoire en utilisant Pandas
df = pd.read_csv(r"C:\Users\Maxime\PycharmProjects\ProjetE3FIAccidentsMortels\data\carcteristiques-2021.csv", sep=";")

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
    folium.CircleMarker(location=[float(row['lat']), float(row['long'])], radius=1, color='#ff0000').add_to(m)

# Affichez la carte
m.save(outfile=r"C:\Users\Maxime\PycharmProjects\ProjetE3FIAccidentsMortels\map.html")
"""
import folium

# Créez une base de carte avec une latitude et une longitude centrales
m = folium.Map(location=[46.52863469527167, 2.43896484375], zoom_start=6)

# Ajoutez les limites des départements de GeoJSON à la carte
folium.GeoJson(
    # Vos données de GeoJSON
    r'C:\Users\Maxime\PycharmProjects\ProjetE3FIAccidentsMortels\data\departements.geojson',
    style_function=lambda feature: {
        'fillColor': '#ffffff',
        'color': '#0000ff',
        'weight': 2,
        'dashArray': '5, 5'
    }
).add_to(m)

# Affichez la carte
m.save(outfile=r"C:\Users\Maxime\PycharmProjects\ProjetE3FIAccidentsMortels\map.html")
