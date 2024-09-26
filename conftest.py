import pytest

from data import Data
from stellar_burgers_api import StellarBurgers


@pytest.fixture
def registration_user():
    registration_user_body = {"email": Data.EMAIL_FOR_REG, "password": Data.PASSWORD_FOR_REG, "name": Data.NAME_FOR_REG}
    login_body = {"email": Data.EMAIL_FOR_REG, "password": Data.PASSWORD_FOR_REG}
    response_reg = StellarBurgers.registration_user(registration_user_body)
    token = response_reg.json()["accessToken"]
    yield [registration_user_body, login_body, token]
    StellarBurgers.delete_user(token)
