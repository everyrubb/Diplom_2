import pytest
import requests

from const import Const
from helpers import Helpers


@pytest.fixture(scope='function')
def helpers():
    return Helpers()

@pytest.fixture(scope='function')
def get_token(helpers):
    data = helpers.register_new_user_and_return_login_password()
    response = requests.post(Const.LOGIN_USER, data={
        "email": data[0],
        "password": data[1],
        "name": data[2]
    })
    token = response.json().get("accessToken")
    return token