from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .tag_creator_validator import tag_creator_validator

class MockRequest:
    def __init__(self, json) -> None:
        self.json = json

def test_tag_creator_validator():
    # Mock data to reproduce an "ok" case
    req = MockRequest(json={ "product_code": "12345" })
    # If some exception raise by the validator, we have a problem
    tag_creator_validator(req)

def test_tag_creator_validator_with_error():
    # Mock data to induce error
    req = MockRequest(json={ "product_code": 12345 })
    try:
        tag_creator_validator(req)
        # If error dont raise, we have a problem...
        assert False
    except Exception as exception:
        # If error raised, chack if its a HttpUnprocessableEntityError instance
        # If not, we have a problem
        assert isinstance(exception, HttpUnprocessableEntityError)
