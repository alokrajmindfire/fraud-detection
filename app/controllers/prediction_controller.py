from app.services.prediction_service import PredictionService
from app.logger import logger

service = PredictionService()

def predict_transaction(data):
    logger.info("Request received for prediction")
    return service.predict(data)
