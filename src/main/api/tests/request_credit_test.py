
import pytest
from sqlalchemy.orm import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.credit_crud import CreditCrudDb


@pytest.mark.api
class TestRequestCredit:
    def test_request_credit(self, api_manager: ApiManager, db_session: Session, user_maker):
        response, user = api_manager.credit_steps.request_credit(user_maker.user_1)
        assert response.balance == pytest.approx(user.account_1.balance)

        credit = api_manager.credit_steps.get_credit_history(user)

        assert credit.creditId == response.creditId
        assert credit.accountId == user.account_1.id

        credit_db = CreditCrudDb.get_credit_by_id(db_session, response.creditId)
        assert user.credit.amount == pytest.approx(credit_db.amount)

    def test_request_credit_invalid(self, api_manager: ApiManager, db_session: Session, user_maker):
        api_manager.credit_steps.request_credit_invalid_role(user_maker.user_default)

        credit = CreditCrudDb.get_credit_by_username(db_session, user_maker.user_default.user.username)
        assert not credit
