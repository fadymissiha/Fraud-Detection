import json
from flask import Flask, jsonify, request
import pandas as pd
import cloudpickle as cp

# Load your model.
pipeline = cp.load(open('DecisionTree.pkl', 'rb'))


def isFraudTran(tran):
    df = pd.DataFrame(tran, index=[0])
    isFraud = pipeline.predict(df)[0]
    return str({ 'isFraud': isFraud })

application = Flask(__name__)


@application.route('/')
@application.route('/status')
def status():
    return jsonify({'status': 'ok'})


@application.route('/predictions', methods=['POST'])
def create_prediction():
    data = request.data or '{}'
    body = json.loads(data)
    return jsonify(isFraudTran(body))