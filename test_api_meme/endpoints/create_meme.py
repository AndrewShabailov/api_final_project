import requests
import allure
from endpoints.base_meme import BaseMeme
from data.payloads import login_payload


class CreateMeme(BaseMeme):

    @allure.step('Send POST request for creating meme')
    def create_meme(self, payload):
        self.response = requests.post(
            f'{self.base_url}/meme', json=payload, headers=self.headers
        )
        allure.attach(
            self.response.text,
            name="Response Body",
            attachment_type=allure.attachment_type.JSON
        )
        return self.response


    def login(self, login_payload):
        self.response = requests.post(
            f'{self.base_url}/authorize', json=login_payload
        )
        print(self.response.json())
        return self.response

