from fastapi import APIRouter
from app.controllers.prediction_controller import predict_transaction
from app.schemas.prediction_schema import TransactionInput

router = APIRouter()

@router.post("/")
async def predict(data: TransactionInput):
    return predict_transaction(data)
