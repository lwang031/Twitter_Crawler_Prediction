from flask import Flask, render_template, request
from indexSearch import search
from flask_googlemaps import GoogleMaps
from flask.views import View
import geocoder
import urllib2
import json

app = Flask(__name__)

tweets = ""

app.config['GOOGLEMAPS_KEY'] = "AIzaSyAd8WV2aBmnx0C3ncG-QpVsFn_KvhM-NvU"

GoogleMaps(app)

f = urllib2.urlopen('http://freegeoip.net/json/')
json_string = f.read()
f.close()
location = json.loads(json_string)


@app.route("/")
def main():
    return render_template('index.html')


color_icons = ['blue', 'yellow', 'green', 'red', 'pink', 'purple']

marker = []
from flask_googlemaps import Map, icons


@app.route("/", methods=["POST"])
def mapview():
    text = request.form['text']
    res = search(text, 10)
    tweet = ""
    for r in res:
        tweet += str(r[1]) + " " + r[0] + " " + r[2] + '<br>'
        if not r[2] == '_':
            map_dic = {'icon': None, 'lat': None, 'lng': None, 'infobox': None}
            print r[2]
            g = geocoder.google(r[2])
            lat = g.json['lat']
            lng = g.json['lng']
            map_dic['icon'] = icons.dots.blue
            map_dic['lat'] = lat
            map_dic['lng'] = lng
            map_dic['infobox'] = r[0]
            marker.append(map_dic)
            print marker

    for m in marker:
        print m
    trdmap = Map(
        identifier="trdmap",
        lat=location['latitude'],
        lng=location['longitude'],
        markers=marker
    )
    return render_template('example.html', trdmap=trdmap, tweet=tweet)


if __name__ == "__main__":
    app.run()