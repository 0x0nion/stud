import pytest
from sqlalchemy.orm import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.account_crud import AccountCrudDb


@pytest.mark.api
class TestAccountTransfer:
    def test_account_transfer(self, api_manager: ApiManager, db_session: Session, user_maker):
        user_1 = user_maker()
        user_2 = user_maker()

        response, amount = api_manager.account_steps.account_transfer(user_1, user_2)
        assert (user_1.account_1.balance - amount) == pytest.approx(response.fromAccountIdBalance)

        account_2 = AccountCrudDb.get_account_by_id(db_session, user_2.account_1.id)
        assert round((user_2.account_1.balance + amount), 2) == pytest.approx(account_2.balance)

        user_tx = api_manager.account_steps.get_last_tx_by_account_id(user_1)

        assert user_tx.fromAccountId == user_1.account_1.id
        assert user_tx.toAccountId == user_2.account_1.id


    @pytest.mark.parametrize(
        "amount", [
            300, 499.99, 10_000.01, 12_000
        ]
    )
    def test_account_transfer_invalid(self, api_manager: ApiManager, db_session: Session, user_maker, amount):
        user_1 = user_maker()
        user_2 = user_maker()

        api_manager.account_steps.account_transfer_invalid(user_1, user_2, amount)

        response_1 = AccountCrudDb.get_account_by_id(db_session, user_1.account_1.id)
        response_2 = AccountCrudDb.get_account_by_id(db_session, user_2.account_1.id)

        assert user_1.account_1.balance == response_1.balance
        assert user_2.account_1.balance == response_2.balance

