import allure
import requests

from const import Const, Ingredients, MessageText


class TestCreateOder():

    @allure.title('Проверка успешного создания заказа с авторизацией')
    def test_create_order_with_authorization_successfully(self, get_token):
        token = get_token
        payload = {
            "ingredients": [Ingredients.BUN_R2_D3, Ingredients.MAIN_PROTOSTOMIA, Ingredients.SAUSE_SPICY_X]
        }
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        response = requests.post(Const.CREATE_ORDER, headers=headers, json=payload)
        assert response.status_code == 200
        assert MessageText.CREATE_ORDER in response.text

    @allure.title('Проверка успешного создания заказа без авторизации')
    def test_create_order_without_authorization(self):
        payload = {
            "ingredients": [Ingredients.BUN_R2_D3, Ingredients.MAIN_PROTOSTOMIA, Ingredients.SAUSE_SPICY_X]
        }
        headers = {"Content-type": "application/json"}
        response = requests.post(Const.CREATE_ORDER, headers=headers, json=payload)
        assert response.status_code == 200
        assert MessageText.CREATE_ORDER in response.text

    @allure.title('Проверка создания заказа без ингредиентов')
    def test_create_order_without_ingredients(self):
        payload = {
            "ingredients": []
        }
        headers = {"Content-type": "application/json"}
        response = requests.post(Const.CREATE_ORDER, headers=headers, json=payload)
        assert response.status_code == 400
        assert MessageText.CREATE_ORDER_WITHOUT_INGREDIENTS in response.text

    @allure.title('Проверка создания заказа с неправильным хешем ингредиента')
    def test_create_order_incorrect_ingredients(self):
        payload = {
            "ingredients": [Ingredients.BUN_R2_D3, Ingredients.MAIN_PROTOSTOMIA, Ingredients.INCORRECT_INGTEDIENTS]
        }
        headers = {"Content-type": "application/json"}
        response = requests.post(Const.CREATE_ORDER, headers=headers, json=payload)
        assert response.status_code == 500
        assert MessageText.CREATE_ORDER_INCORRECT_INGTEDIENTS in response.text
