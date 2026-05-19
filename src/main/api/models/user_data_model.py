from typing import Optional

from src.main.api.models.base_model import BaseModel
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.create_user_request import CreateUserRequest


class UserData(BaseModel):
    user: CreateUserRequest
    account_1: CreateAccountResponse
    account_2: Optional[CreateAccountResponse]


