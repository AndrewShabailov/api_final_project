import requests
import allure
from data.payloads import payload
from endpoints.base_meme import BaseMeme

class CreateMeme(BaseMeme):

    @allure.step('Send POST request for creating meme')
    def create_meme(self, payload):
        self.response = requests.post(
            f'{self.base_url}/meme', json=payload, headers=self.headers
        )
        allure.attach(self.response.text, name="Response Body", attachment_type=allure.attachment_type.JSON)
        return self.response
