import requests
from requests import Response

from src.main.api.models.deposit_account_response import DepositAccountResponse
from src.main.api.requests.requester import Requester


class DepositAccountRequester(Requester):
    def post(self, model=None) -> DepositAccountResponse | Response:
        url = f"{self.base_url}/account/create"

        response = requests.post(
            url=url,
            headers=self.headers
        )

        self.response_spec(response)
        return DepositAccountResponse(**response.json())