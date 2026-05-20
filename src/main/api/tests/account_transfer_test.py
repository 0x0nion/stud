import pytest
from sqlalchemy.orm import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.account_crud import AccountCrudDb


@pytest.mark.api
class TestAccountTransfer:
    def test_account_transfer(self, api_manager: ApiManager, db_session: Session, user_maker):
        response, u1, u2 = api_manager.account_steps.account_transfer(user_maker.user_1, user_maker.user_2)

        assert u1.account_1.balance == pytest.approx(response.fromAccountIdBalance)

        account_2 = AccountCrudDb.get_account_by_id(db_session, u2.account_1.id)
        assert round(u2.account_1.balance, 2) == pytest.approx(account_2.balance)

        user_tx = api_manager.account_steps.get_last_tx_by_account_id(u1)

        assert user_tx.fromAccountId == u1.account_1.id
        assert user_tx.toAccountId == u2.account_1.id

    @pytest.mark.parametrize(
        "amount", [
            300, 499.99, 10_000.01, 12_000
        ]
    )
    def test_account_transfer_invalid(self, api_manager: ApiManager, db_session: Session, user_maker, amount):
        api_manager.account_steps.account_transfer_invalid(user_maker.user_1, user_maker.user_2, amount)

        response_1 = AccountCrudDb.get_account_by_id(db_session, user_maker.user_1.account_1.id)
        response_2 = AccountCrudDb.get_account_by_id(db_session, user_maker.user_2.account_1.id)

        assert user_maker.user_1.account_1.balance == response_1.balance
        assert user_maker.user_2.account_1.balance == response_2.balance

