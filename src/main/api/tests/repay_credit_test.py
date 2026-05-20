import pytest
from sqlalchemy.orm import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.credit_crud import CreditCrudDb


@pytest.mark.api
class TestRepayCredit:
    def test_repay_credit(self, api_manager: ApiManager, db_session: Session, user_maker):
        response = api_manager.credit_steps.repay_credit(user_maker.user_with_credit)

        assert response.creditId == user_maker.user_with_credit.credit.creditId
        assert response.amountDeposited == pytest.approx(user_maker.user_with_credit.credit.amount)

    def test_repay_credit_invalid(self, api_manager: ApiManager, db_session: Session, user_maker):

        api_manager.credit_steps.repay_credit_invalid(user=user_maker.user_with_credit)

        credit = CreditCrudDb.get_credit_by_username(db_session, user_maker.user_with_credit.user.username)

        assert credit.amount == pytest.approx(user_maker.user_with_credit.credit.amount)
        assert credit.id == user_maker.user_with_credit.credit.creditId
