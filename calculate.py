from flask import Flask, request, redirect, url_for, flash, jsonify
import json

application = Flask(__name__)
    
@application.route('/calculate', methods=['POST'])
def calculate():
    #Processing request data
    payload = request.get_json()
    model_name = payload['model_name']
    inputs = payload['inputs']
    # Fake model run here
    result = inputs['x'] + inputs['y']

    return jsonify(result)

if __name__ == '__main__':
    application.run()
