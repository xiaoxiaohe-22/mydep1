import requests

import app


class LoginApi(object):

    def __init__(self):
        self.login_url = app.URL+"/api/sys/login"

    def login(self, data):
        return requests.post(url=self.login_url, json=data)
