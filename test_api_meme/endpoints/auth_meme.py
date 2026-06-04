import requests
import allure
from endpoints.base_meme import BaseMeme


class AuthMeme(BaseMeme):

    @allure.step('Send POST request for authorization')
    def login(self, login_payload):
        self.response = requests.post(
            f'{self.base_url}/authorize', json=login_payload
        )
        return self.response
