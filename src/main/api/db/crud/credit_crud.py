from sqlalchemy.orm import Session

from src.main.api.db.models.account_table import Account
from src.main.api.db.models.credit_table import Credit
from src.main.api.db.models.user_table import User


class CreditCrudDb:
    @staticmethod
    def get_credit_by_id(db: Session, credit_id: int) -> Credit | None:
        return db.query(Credit).filter_by(id=credit_id).first()

    @staticmethod
    def get_credit_by_username(db: Session, username: str) -> Credit | None:
        return db.query(Credit).join(Account).join(User).filter(User.username == username).first()
