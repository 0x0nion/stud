import random

import pytest
from sqlalchemy.orm import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.credit_crud import CreditCrudDb


@pytest.mark.api
class TestRepayCredit:
    def test_repay_credit(self, api_manager: ApiManager, db_session: Session, user_maker):
        user = user_maker(credit=True)
        credit_info, amount = api_manager.credit_steps.request_credit(user)

        response = api_manager.credit_steps.repay_credit(user=user, amount=amount, credit_id=credit_info.creditId)

        assert response.creditId == credit_info.creditId
        assert response.amountDeposited == pytest.approx(amount)

    def test_repay_credit_invalid(self, api_manager: ApiManager, db_session: Session, user_maker):
        user = user_maker(credit=True)
        credit_info, amount = api_manager.credit_steps.request_credit(user)

        repay_amount = amount * 0.9

        api_manager.credit_steps.repay_credit_invalid(user=user, amount=repay_amount, credit_id=credit_info.creditId)

        credit = CreditCrudDb.get_credit_by_username(db_session, user.user.username)

        assert credit.amount == pytest.approx(amount)
        assert credit.id == credit_info.creditId
