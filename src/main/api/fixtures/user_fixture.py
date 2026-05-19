import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.generators.user_generator import UserGenerator
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.user_data_model import UserData


@pytest.fixture
def create_user_request(api_manager: ApiManager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request


@pytest.fixture
def create_user_with_account(api_manager: ApiManager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    account_response = api_manager.user_steps.create_account(user_request)

    return UserData(
        user=user_request,
        account_1=account_response,
        account_2=None,

    )


@pytest.fixture
def create_user_max_accounts(api_manager: ApiManager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    account1_response = api_manager.user_steps.create_account(user_request)
    account2_response = api_manager.user_steps.create_account(user_request)

    return UserData(
        user=user_request,
        account_1=account1_response,
        account_2=account2_response
    )


@pytest.fixture
def user_maker(api_manager: ApiManager):
    factory = UserGenerator(api_manager)

    def _make(credit=False):
        if credit:
            return factory.generate_credit_user()
        return factory.generate()

    return _make

