import allure

import response_message
from stellar_burgers_api import StellarBurgers


class TestGetOdersUser:

    @allure.title('Получение заказов авторизованного пользователя :api/orders')
    def test_get_orders_auth_user(self, registration_user):
        response = StellarBurgers.get_order_auth_user(registration_user[2])
        assert response.status_code == 200 and response_message.TRUE in response.text

    @allure.title('Получение заказов неавторизованного пользователя :api/orders')
    def test_get_orders_no_auth_user(self):
        response = StellarBurgers.get_order_no_auth_user()
        assert response.status_code == 401 and response_message.ERROR_NO_AUTHORIZATION in response.text
