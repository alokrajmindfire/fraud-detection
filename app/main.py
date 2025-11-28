from fastapi import FastAPI
from app.routes.prediction_routes import router as prediction_router
from app.logger import logger

app = FastAPI(title="Credit Card Fraud Detection API")

@app.get("/")
def root():
    logger.info("Root endpoint called")
    return {"msg": "Fraud Detection API is running"}

app.include_router(prediction_router, prefix="/api/v1/predict")
