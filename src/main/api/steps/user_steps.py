from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.validate_crud_requster import ValidateCrudRequester
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps


class UserSteps(BaseSteps):
    def create_account(self, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            request_spec=RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            endpoint=Endpoint.USER_CREATE_ACCOUNT,
            response_spec=ResponseSpecs.request_created()
        ).post()
        return response

    def create_account_invalid(self, create_user_request: CreateUserRequest):
        acc = 0
        while acc < 3:
            acc += 1
            requester = ValidateCrudRequester(
                request_spec=RequestSpecs.auth_headers(username=create_user_request.username,
                                                       password=create_user_request.password),
                endpoint=Endpoint.USER_CREATE_ACCOUNT,
                response_spec=ResponseSpecs.request_conflict() if acc > 2 else ResponseSpecs.request_created()
            )

            if acc <= 2:
                requester.post()
            else:
                response = requester.crud_requester.post(None)
                requester.response_spec(response)
                return response

