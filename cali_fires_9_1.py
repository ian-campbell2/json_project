import json

in_file = open('US_fires_9_1.json','r')

fire_data = json.load(in_file)

lats, lons, brights = [],[],[]

for x in fire_data:
    lat = x['latitude']
    lon = x['longitude']
    bright = x['brightness']
    if x['brightness'] > 450:
        lons.append(lon)
        lats.append(lat)
        brights.append(bright)

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'brightness': brights,
    'marker': {
        'size':[5*x for x in brights],
        'color': brights,
        'colorscale': 'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Brightness'}

    },

}]

my_layout = Layout(title='US Wildfires Sep/1 - Sep/13')

fig = {'data':data, 'layout':my_layout}

offline.plot(fig, filename='US_Wildfires_9_1.html')