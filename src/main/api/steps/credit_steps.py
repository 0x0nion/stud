import random

import pytest

from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.foundation.requesters.validate_crud_requster import ValidateCrudRequester
from src.main.api.models.account_transfer_request import AccountTransferRequest
from src.main.api.models.credit_repay_requset import CreditRepayRequest
from src.main.api.models.credit_request_request import CreditRequestRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.user_data_model import UserData
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps


class CreditSteps(BaseSteps):
    def request_credit(self, user: UserData):
        amount = round(random.uniform(5000, 15000), 2)

        credit_request_request = CreditRequestRequest(
            accountId=user.account_1.id,
            amount=amount,
            termMonths=random.randint(1, 60)
        )

        response = ValidateCrudRequester(
            request_spec=RequestSpecs.auth_headers(
                username=user.user.username,
                password=user.user.password
            ),
            endpoint=Endpoint.CREDIT_REQUEST,
            response_spec=ResponseSpecs.request_created()
        ).post(credit_request_request)

        return response, amount

    def request_credit_invalid_role(self, user: UserData):
        amount = round(random.uniform(5000, 15000), 2)

        credit_request_request = CreditRequestRequest(
            accountId=user.account_1.id,
            amount=amount,
            termMonths=random.randint(1, 60)
        )

        CrudRequester(
            request_spec=RequestSpecs.auth_headers(
                username=user.user.username,
                password=user.user.password
            ),
            endpoint=Endpoint.CREDIT_REQUEST,
            response_spec=ResponseSpecs.request_forbidden()
        ).post(credit_request_request)

    def repay_credit(self, user: UserData, amount: float, credit_id: int):
        credit_repay_request = CreditRepayRequest(
            creditId=credit_id,
            accountId=user.account_1.id,
            amount=amount
        )

        response = ValidateCrudRequester(
            request_spec=RequestSpecs.auth_headers(
                username=user.user.username,
                password=user.user.password
            ),
            endpoint=Endpoint.CREDIT_REPAY,
            response_spec=ResponseSpecs.request_ok()
        ).post(credit_repay_request)

        return response

    def repay_credit_invalid(self, user: UserData, amount: float, credit_id: int):
        credit_repay_request = CreditRepayRequest(
            creditId=credit_id,
            accountId=user.account_1.id,
            amount=amount
        )

        CrudRequester(
            request_spec=RequestSpecs.auth_headers(
                username=user.user.username,
                password=user.user.password
            ),
            endpoint=Endpoint.CREDIT_REPAY,
            response_spec=ResponseSpecs.requset_unprocessable_entity()
        ).post(credit_repay_request)

    def get_credit_history(self, user: UserData):
        response = ValidateCrudRequester(
            request_spec=RequestSpecs.auth_headers(
                username=user.user.username,
                password=user.user.password
            ),
            endpoint=Endpoint.CREDIT_HISTORY,
            response_spec=ResponseSpecs.request_ok()
        ).get()

        return response.credits[0]