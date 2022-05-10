import json
from flask import Flask, jsonify, request
from prediction import predict, predictRF

application = Flask(__name__)


@application.route('/')
@application.route('/status')
def status():
    return jsonify({'status': 'ok'})


@application.route('/predictions', methods=['POST'])
def create_prediction():
    data = request.data or '{}'
    body = json.loads(data)
    return jsonify(predict(body))

@application.route('/predictionsRF', methods=['POST'])
def create_prediction():
    data = request.data or '{}'
    body = json.loads(data)
    return jsonify(predictRF(body))
