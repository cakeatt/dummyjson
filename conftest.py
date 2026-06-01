import pytest
from common.api_client import ApiClient,AnonymousClient
from common.config import TEST_USER

@pytest.fixture(scope="session")
def anonymous():
    return AnonymousClient()

@pytest.fixture(scope="session")
def api_client():
    client=ApiClient()
    client.login(TEST_USER['username'],TEST_USER['password'])
    return client