from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

with open("video_games.json", "r") as f:
    game_data = json.loads(f.read())

@app.route("/test", methods=['GET'])
def test():
    data = {
        'name': 'eric'
    }
    response = make_response(data)
    # response.headers.add("Access-Control-Allow-Origin", "*")
    # response.headers.add("Access-Control-Allow-Headers", "*")
    # response.headers.add("Access-Control-Allow-Methods", "*")
    return response


@app.route("/rec", methods=['GET', 'POST'])
def recommendations():
    data = json.loads(request.data.decode('utf-8'))
    new_data = {
        'fullName': data['name'] + " zhou",
        'newAge': data['age'] + 5,
    }
    game = game_data[0]
    print(game['Title'])
    print(game['Metadata'])
    return new_data
    

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
