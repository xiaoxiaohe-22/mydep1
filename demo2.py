import unittest
import requests


class  TestLogin(unittest.TestCase):
    @classmethod
    def  setUpClass(cls):
        cls.login_url = "http://ihrm-test.itheima.net/api/sys/login"

    def test_01_login(self):
        data = {"mobile": "13800000002", "password": "123456"}
        response = requests.post(url=self.login_url, json=data)
        print(response.json())
        self.assertIn("操作成功",response.json().get("message"))

