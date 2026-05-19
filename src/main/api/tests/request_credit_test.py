
import pytest
from sqlalchemy.orm import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.credit_crud import CreditCrudDb


@pytest.mark.api
class TestRequestCredit:
    def test_request_credit(self, api_manager: ApiManager, db_session: Session, user_maker):
        user = user_maker(credit=True)
        response, amount = api_manager.credit_steps.request_credit(user)
        assert response.balance == pytest.approx(user.account_1.balance + amount)

        credit = api_manager.credit_steps.get_credit_history(user)

        assert credit.creditId == response.creditId
        assert credit.termMonths == response.termMonths
        assert credit.creditId == response.creditId

        credit_db = CreditCrudDb.get_credit_by_id(db_session, response.creditId)
        assert amount == pytest.approx(credit_db.amount)

    def test_request_credit_invalid(self, api_manager: ApiManager, db_session: Session, user_maker):
        user = user_maker()
        api_manager.credit_steps.request_credit_invalid_role(user)

        credit = CreditCrudDb.get_credit_by_username(db_session, user.user.username)
        assert not credit
