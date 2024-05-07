import allure
import requests

from const import Const, MessageText

class TestLoginUser:


    @allure.title('Проверка авторизации пользователя')
    def test_login_user_successfully(self, helpers):
        data = helpers.register_new_user_and_return_login_password()
        response = requests.post(Const.LOGIN_USER, data={
            "email": data[0],
            "password": data[1],
        })
        assert response.status_code == 200
        assert MessageText.LOGIN_USER in response.text

    @allure.title('Проверка авторизации пользователя с неверным логином ')
    def test_login_user_incorrect_login(self, helpers):
        data = helpers.register_new_user_and_return_login_password()
        response = requests.post(Const.LOGIN_USER, data={
            "email": data[1],
            "password": data[2],
        })
        assert response.status_code == 401
        assert MessageText.INCORECT_LOGIN_DATA in response.text

    @allure.title('Проверка авторизации пользователя с неверным паролем')
    def test_login_user_incorrect_password(self, helpers):
        data = helpers.register_new_user_and_return_login_password()
        response = requests.post(Const.LOGIN_USER, data={
            "email": data[0],
            "password": data[2],
        })
        assert response.status_code == 401
        assert MessageText.INCORECT_LOGIN_DATA in response.text
