import json



in_file = open('eq_data_1_day_m1.json','r')

out_file = open('readable_eq_data.json','w')

eq_data = json.load(in_file)
#converts json into python file

json.dump(eq_data, out_file, indent=4)
#organizes file to make it readable, saves as out_file

list_of_eqs = eq_data['features']

print(type(list_of_eqs))

print(len(list_of_eqs))

mags, lons, lats = [],[],[]
'''
print(list_of_eqs[0]['properties']['mag'])
print(list_of_eqs[0]['geometry']['coordinates'][1])
print(list_of_eqs[0]['geometry']['coordinates'][0])

'''
for eq in list_of_eqs:
    mag = eq['properties']['mag']
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print('Mags')
print(mags[:10])
print('Lons')
print(lons[:10])
print('Lats')
print(lats[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
'''
data = [Scattergeo(lon=lons, lat=lats)]
'''
data = [{
    'type': Scattergeo,
    'lon': lons,
    'lat': lats,
    'marker': {
        'size':[5*mag for mag in mags],
    },

}]
my_layout = Layout(title='global earthquakes')

fig = {'data': data, 'layout':my_layout}

offline.plot(fig, filename='global_earthquake.html')