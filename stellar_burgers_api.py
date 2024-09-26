import requests

import urls


class StellarBurgers:

    @staticmethod
    def registration_user(body):
        return requests.post(urls.BASE_URL + urls.REGISTRATION_USER_ENDPOINT, json=body)

    @staticmethod
    def auth_user(body):
        return requests.post(urls.BASE_URL + urls.AUTH_ENDPOINT, json=body)

    @staticmethod
    def change_user(token, body):
        return requests.patch(urls.BASE_URL + urls.CHANGE_USER_ENDPOINT, headers={'Authorization': token}, json=body)

    @staticmethod
    def change_user_no_autorization(body):
        return requests.patch(urls.BASE_URL + urls.CHANGE_USER_ENDPOINT, json=body)

    @staticmethod
    def creating_order_ingredient(body):
        response = requests.post(urls.BASE_URL + urls.CREATING_ORDER_ENDPOINT, json={"ingredients": [body]})
        return response

    def creating_order_no_ingredient():
        return requests.post(urls.BASE_URL + urls.CREATING_ORDER_ENDPOINT)

    @staticmethod
    def get_order_auth_user(token):
        return requests.get(urls.BASE_URL + urls.GET_ORDER_USER_ENDPOINT, headers={'Authorization': token})

    @staticmethod
    def get_order_no_auth_user():
        return requests.get(urls.BASE_URL + urls.CHANGE_USER_ENDPOINT)

    @staticmethod
    def delete_user(token):
        return requests.delete(urls.BASE_URL + urls.DELETE_USER_ENDPOINT, headers={'Authorization': token})

    @staticmethod
    def get_ingedients():
        return requests.get(urls.BASE_URL + urls.GET_INGREDIENTS_ENDPOINT)
