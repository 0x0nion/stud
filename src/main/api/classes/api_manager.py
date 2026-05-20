from typing import List, Any

from src.main.api.steps.admin_steps import AdminSteps
from src.main.api.steps.credit_steps import CreditSteps
from src.main.api.steps.user_steps import UserSteps
from src.main.api.steps.account_steps import AccountSteps


class ApiManager:
    def __init__(self, created_object: List[Any]):
        self.admin_steps = AdminSteps(created_object)
        self.user_steps = UserSteps(created_object)
        self.account_steps = AccountSteps(created_object)
        self.credit_steps = CreditSteps(created_object)

