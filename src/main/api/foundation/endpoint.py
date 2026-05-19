from dataclasses import dataclass
from enum import Enum
from typing import Type, Optional

from src.main.api.models.account_transfer_request import AccountTransferRequest
from src.main.api.models.account_transfer_response import AccountTransferResponse
from src.main.api.models.account_tx_response import AccountTxResponse
from src.main.api.models.base_model import BaseModel
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_user_response import CreateUserResponse
from src.main.api.models.credit_history_response import CreditHistoryResponse
from src.main.api.models.credit_repay_requset import CreditRepayRequest
from src.main.api.models.credit_repay_response import CreditRepayResponse
from src.main.api.models.credit_request_request import CreditRequestRequest
from src.main.api.models.credit_request_response import CreditRequestResponse
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.deposit_account_response import DepositAccountResponse
from src.main.api.models.login_user_request import LoginUserRequest
from src.main.api.models.login_user_response import LoginUserResponse


@dataclass
class EndpointConfiguration:
    url: str
    request_model: Optional[Type[BaseModel]]
    response_model: Optional[Type[BaseModel]]


class Endpoint(Enum):
    ADMIN_CREATE_USER = EndpointConfiguration(
        request_model=CreateUserRequest,
        response_model=CreateUserResponse,
        url="/admin/create"
    )

    ADMIN_DELETE_USER = EndpointConfiguration(
        request_model=None,
        response_model=None,
        url="/admin/users/"
    )

    LOGIN_USER = EndpointConfiguration(
        request_model=LoginUserRequest,
        response_model=LoginUserResponse,
        url="/auth/token/login"
    )

    USER_CREATE_ACCOUNT = EndpointConfiguration(
        request_model=None,
        response_model=CreateAccountResponse,
        url="/account/create"
    )

    ACCOUNT_DEPOSIT = EndpointConfiguration(
        response_model=DepositAccountResponse,
        request_model=DepositAccountRequest,
        url="/account/deposit"
    )

    ACCOUNT_TRANSFER = EndpointConfiguration(
        request_model=AccountTransferRequest,
        response_model=AccountTransferResponse,
        url='/account/transfer'
    )

    ACCOUNT_GET_TX = EndpointConfiguration(
        request_model=None,
        response_model=AccountTxResponse,
        url="/account/transactions/"
    )

    CREDIT_REQUEST = EndpointConfiguration(
        request_model=CreditRequestRequest,
        response_model=CreditRequestResponse,
        url="/credit/request"
    )

    CREDIT_REPAY = EndpointConfiguration(
        request_model=CreditRepayRequest,
        response_model=CreditRepayResponse,
        url="/credit/repay"
    )

    CREDIT_HISTORY = EndpointConfiguration(
        request_model=None,
        response_model=CreditHistoryResponse,
        url="/credit/history"
    )
