import geocoder
g = geocoder.google('Los Angeles, CA')
lat = g.json['lat']
lng = g.json['lng']