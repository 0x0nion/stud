import random
from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.foundation.requesters.validate_crud_requster import ValidateCrudRequester
from src.main.api.models.account_transfer_request import AccountTransferRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.user_data_model import UserData
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps


class AccountSteps(BaseSteps):
    def deposit_account(self, user_data: UserData, amount=None):
        if not amount:
            amount = random.uniform(1000, 9000)

        deposit_account_request = DepositAccountRequest(
            accountId=user_data.account_1.id,
            amount=round(amount, 2)
        )

        response = ValidateCrudRequester(
            request_spec=RequestSpecs.auth_headers(username=user_data.user.username,
                                                   password=user_data.user.password),
            endpoint=Endpoint.ACCOUNT_DEPOSIT,
            response_spec=ResponseSpecs.request_ok()
        ).post(deposit_account_request)

        return response, round(amount, 2)

    def deposit_account_invalid(self, user_data: UserData, amount):
        deposit_account_request = DepositAccountRequest(
            accountId=user_data.account_1.id,
            amount=amount
        )

        response = CrudRequester(
            request_spec=RequestSpecs.auth_headers(username=user_data.user.username,
                                                   password=user_data.user.password),
            endpoint=Endpoint.ACCOUNT_DEPOSIT,
            response_spec=ResponseSpecs.request_bad()
        ).post(deposit_account_request)

        return response, amount

    def account_transfer(self, user_1: UserData, user_2: UserData):
        amount = round(random.uniform(500, 10_000), 2)

        if amount >= user_1.account_1.balance:
            amount = user_1.account_1.balance

        account_transfer_request = AccountTransferRequest(
            fromAccountId=user_1.account_1.id,
            toAccountId=user_2.account_1.id,
            amount=amount
        )

        response = ValidateCrudRequester(
            request_spec=RequestSpecs.auth_headers(
                username=user_1.user.username,
                password=user_1.user.password
            ),
            endpoint=Endpoint.ACCOUNT_TRANSFER,
            response_spec=ResponseSpecs.request_ok()
        ).post(account_transfer_request)

        return response, amount

    def account_transfer_invalid(self, user_1: UserData, user_2: UserData, amount: float):
        account_transfer_request = AccountTransferRequest(
            fromAccountId=user_1.account_1.id,
            toAccountId=user_2.account_1.id,
            amount=amount
        )

        CrudRequester(
            request_spec=RequestSpecs.auth_headers(
                username=user_1.user.username,
                password=user_1.user.password
            ),
            endpoint=Endpoint.ACCOUNT_TRANSFER,
            response_spec=ResponseSpecs.request_bad()
        ).post(account_transfer_request)

    def get_last_tx_by_account_id(self, user: UserData):
        response = ValidateCrudRequester(
            request_spec=RequestSpecs.auth_headers(
                username=user.user.username,
                password=user.user.password
            ),
            endpoint=Endpoint.ACCOUNT_GET_TX,
            response_spec=ResponseSpecs.request_ok()
        ).get(query=str(user.account_1.id))

        return response.transactions[0]
