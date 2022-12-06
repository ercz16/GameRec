from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import json
from shellsort import shellsort
from tim_sort import tim_sort
import copy

app = Flask(__name__)
CORS(app)

with open("video_games.json", "r") as f:
    game_data = json.loads(f.read())

@app.route("/shellsort", methods=['GET', 'POST'])
def get_shell_sort():
    print("shellsort")
    # Receive payload
    payload = json.loads(request.data.decode('utf-8'))

    # Destructure payload + tuple conversions
    genres = payload['genres']
    priceRange = tuple(payload['priceRange'])
    timeRange = tuple(payload['timeRange'])
    online = payload['online']

    # Load copy of game_data
    copy_data = copy.deepcopy(game_data)
    return shellsort(genres, priceRange, timeRange, online, copy_data)


@app.route("/timsort", methods=['GET', 'POST'])
def get_tim_sort():
    print("timsort")
    # Receive payload
    payload = json.loads(request.data.decode('utf-8'))

    # Destructure payload + tuple conversions
    genres = payload['genres']
    priceRange = tuple(payload['priceRange'])
    timeRange = tuple(payload['timeRange'])
    online = payload['online']

    # Load copy of game_data
    copy_data = copy.deepcopy(game_data)
    return tim_sort(copy_data, genres, priceRange, timeRange, online)
    

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
