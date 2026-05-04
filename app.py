from flask import Flask, jsonify
from model import predict_future

app = Flask(__name__)

@app.route('/')
def home():
    return "BharatAcre AI Server Running"

@app.route('/predict')
def predict():
    result = predict_future()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)