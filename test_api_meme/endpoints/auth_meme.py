import allure
import requests
from endpoints.base_meme import BaseMeme


class AuthMeme(BaseMeme):

    @allure.step('Send POST request to authorize')
    def login(self, payload):
        self.response = requests.post(f'{self.base_url}/authorize', json=payload)
        return self.response

    @allure.step('Send GET request to validate token')
    def check_token_alive(self, token):
        self.response = requests.get(f'{self.base_url}/authorize/{token}')
        return self.response
