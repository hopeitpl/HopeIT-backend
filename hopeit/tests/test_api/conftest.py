import pytest
from falcon import testing

from hopeit.api.api import configure_api


@pytest.fixture()
def client(hopeit):
    api = configure_api()
    return testing.TestClient(api)
