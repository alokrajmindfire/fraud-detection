import requests

API_URL = "http://localhost:8000/api/v1/predict/"

def predict_api(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()
