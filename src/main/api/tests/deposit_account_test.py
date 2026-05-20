import pytest
from sqlalchemy.orm import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.account_crud import AccountCrudDb


@pytest.mark.api
class TestDepositAccount:
    def test_deposit_valid(self, api_manager: ApiManager, db_session: Session, create_user_with_account):
        response, amount = api_manager.account_steps.deposit_account(
            user_data=create_user_with_account
        )

        assert response.balance == create_user_with_account.account_1.balance + amount

        account_from_db = AccountCrudDb.get_account_by_id(db_session, response.id)

        assert account_from_db.balance == create_user_with_account.account_1.balance + amount

    @pytest.mark.parametrize(
        "amount", [
            100, 999.99, 9000.01, 10000
        ]
    )
    def test_deposit_invalid(self, api_manager: ApiManager, db_session: Session, create_user_with_account, amount):
        api_manager.account_steps.deposit_account_invalid(
            user_data=create_user_with_account,
            amount=amount
        )
        account_from_db = AccountCrudDb.get_account_by_id(db_session, create_user_with_account.account_1.id)
        assert account_from_db.balance == create_user_with_account.account_1.balance

