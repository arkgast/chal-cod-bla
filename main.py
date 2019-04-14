import threading
from flask import Flask
from flask import jsonify

from info import data
from stream_data import main


class Thread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        main()


# create application
app = Flask(__name__)
prev_list = list()


@app.route('/')
def index():
    t = Thread()
    t.start()
    return 'Running'


@app.route('/data')
def stream():
    '''
    GeoJSON Format
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [125.6, 10.1]
      },
      "properties": {
        "name": "Dinagat Islands"
      }
    }
    '''
    new_data = []
    for item in data:
        temp_data = {}
        temp_data['geometry'] = {}
        temp_data['properties'] = {}
        temp_data['type'] = 'Feature'
        temp_data['geometry']['type'] = 'Point'
        temp_data['geometry']['coordinates'] = item['coordinates']['coordinates']
        temp_data['properties']['name'] = item['text']
        new_data.append(temp_data)

    global prev_list

    prev_list = prev_list + new_data
    return jsonify(prev_list)


if __name__ == "__main__":
    app.run(debug=True, threaded=True, host="0.0.0.0", port=5000)
