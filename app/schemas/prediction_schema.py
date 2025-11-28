from pydantic import BaseModel

class TransactionInput(BaseModel):
    Amount: float
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
