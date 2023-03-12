from math import lgamma
from turtle import color
from click import style
import folium
import pandas as pd

data = pd.read_csv('Volcanoes.txt')

lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

def color_prducer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[45.94, 25.00], zoom_start=6, tiles='Stamen Terrain')

fgv = folium.FeatureGroup(name='Volacanoes')

for lt, lg, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, lg], radius=6, fill=True, fill_color=color_prducer(el), fill_opacity=0.7,
    color='grey', popup=folium.Popup(str(el) + ' meters')))

# icon=folium.Icon(color=color_prducer(el))

fgp = folium.FeatureGroup(name='Polpulation')

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
                            style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 
                            else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                            else 'red'}))

map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())

map.save('Map1.html')