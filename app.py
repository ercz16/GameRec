from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

@app.route("/test", methods=['GET'])
def recommendations():
    app.logger.warning('whattt')
    if request.method == 'GET':
        data = {
            'name': 'eric',
            'age': 20,
        }
        app.logger.warning('testing warning log')
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
