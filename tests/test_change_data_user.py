import allure

import response_message
from data import Data
from stellar_burgers_api import StellarBurgers


class TestChangeDataUser:

    @allure.title('Успешное изменение данных пользователя c авторизацией :api/auth/user')
    def test_change_data_auth_user(self, registration_user):
        StellarBurgers.auth_user(registration_user[1])
        response = StellarBurgers.change_user(registration_user[2], Data.DATA_CHANGE)
        assert response.status_code == 200 and response_message.TRUE in response.text

    @allure.title('Изменение данных пользователя без авторизации :api/auth/user')
    def test_change_data_unauthorized_user(self, registration_user):
        response = StellarBurgers.change_user_no_autorization(Data.DATA_CHANGE)
        assert response.status_code == 401 and response_message.ERROR_NO_AUTHORIZATION in response.text
