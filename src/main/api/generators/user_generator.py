from src.main.api.classes.api_manager import ApiManager
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request import CreateUserRequest, UserRole
from src.main.api.models.user_data_model import UserData


class UserGenerator:
    def __init__(self, api_manager: ApiManager):
        self.api_manager = api_manager

    def _create_user(self, credit=False):
        user_request = RandomModelGenerator.generate(CreateUserRequest)
        if credit:
            user_request.role = UserRole.ROLE_CREDIT_SECRET
        self.api_manager.admin_steps.create_user(user_request)
        return user_request

    def _accounts(self, user_request):
        account1_response = self.api_manager.user_steps.create_account(user_request)
        account2_response = self.api_manager.user_steps.create_account(user_request)
        return account1_response, account2_response

    def _deposit(self, user):
        _, amount = self.api_manager.account_steps.deposit_account(user)
        user.account_1.balance = amount
        return user

    def _get_credit(self, user):
        response, user = self.api_manager.credit_steps.request_credit(user)
        user.credit = response
        return user

    def _complete_user(self, user_request, with_credit=False):
        account1_response, account2_response = self._accounts(user_request)

        credit = None
        user = UserData(
            user=user_request,
            account_1=account1_response,
            account_2=account2_response,
            credit=credit
        )

        user = self._deposit(user)

        if with_credit:
            user = self._get_credit(user)
        return user

    def _generate(self, credit=False, with_credit=False):
        user_request = self._create_user(credit)
        return self._complete_user(user_request, with_credit)

    @property
    def user_1(self):
        return self._generate(credit=True)

    @property
    def user_2(self):
        return self._generate(credit=True)

    @property
    def user_default(self):
        return self._generate()

    @property
    def user_with_credit(self):
        return self._generate(credit=True, with_credit=True)
