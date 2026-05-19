import datetime
from enum import Enum
from sqlalchemy import ForeignKey, Column, Integer, Float, DateTime, func, String
from src.main.api.db.base import Base


class TransactionType(str, Enum):
    DEPOSIT = "deposit"
    TRANSFER_IN = "transfer_in"
    TRANSFER_OUT = "transfer_out"
    CREDIT_ISSUANCE = "credit_issuance"


class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, autoincrement=True)
    to_account_id = Column(Integer, ForeignKey('account.id'), nullable=True)
    from_account_id = Column(Integer, ForeignKey('account.id'), nullable=True)
    credit_id = Column(Integer, ForeignKey('credit.id'), nullable=True)
    amount = Column(Float, nullable=False)
    transaction_type = Column(TransactionType, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now)

    def __repr__(self):
        return (f"<Transaction(id={self.id}, to_account_id={self.to_account_id}, from_account_id={self.from_account_id}, "
                f"credit_id={self.credit_id}, amount={self.amount}, transaction_type={self.transaction_type}, "
                f"created_at={self.created_at}>")
