import logging
import unittest
from parameterized import parameterized
import app
from api.LoginApi import LoginApi
from utils import get_login_data


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login_api = LoginApi()

    @parameterized.expand(get_login_data(app.BASE_PATH + "/data/login.json"))
    def test_01_login(self, mobile, password, message):
        data = {"mobile": mobile, "password": password}
        response = self.login_api.login(data)
        logging.info(response.json())
        # 断言
        self.assertIn(message, response.json().get("message"))
