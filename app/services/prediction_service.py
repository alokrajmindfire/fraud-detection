import pickle
import numpy as np
from app.config import MODEL_PATH, SCALER_PATH
from app.logger import logger

class PredictionService:
    def __init__(self):
        logger.info("Loading model and scaler...")
        self.model = pickle.load(open(MODEL_PATH, "rb"))
        self.scaler = pickle.load(open(SCALER_PATH, "rb"))

    
    def predict(self, data):
        # Convert input to array
        features = np.array(list(data.dict().values())).reshape(1, -1)

        # Scale Amount & Time (columns 0 and 1)
        features[:, [0, 1]] = self.scaler.transform(features[:, [0, 1]])

        # Predict
        prediction = self.model.predict(features)[0]
        proba = self.model.predict_proba(features)[0][1]

        logger.info(f"Prediction: {prediction}, Probability: {proba}")

        return {
            "fraud": bool(prediction),
            "probability": float(proba)
        }
