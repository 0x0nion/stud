from datetime import datetime
from src.main.api.models.base_model import BaseModel


class TxData(BaseModel):
    transactionId: int
    type: str
    amount: float
    fromAccountId: int | None = None
    toAccountId: int
    createdAt: datetime
    creditId: int | None = None


class AccountTxResponse(BaseModel):
    id: int
    number: str
    balance: float
    transactions: list[TxData]
