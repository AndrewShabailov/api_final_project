import requests
import allure
from endpoints.base_meme import BaseMeme


class ReadMeme(BaseMeme):

    @allure.step('Send GET request for reading all memes')
    def read_meme(self):
        self.response = requests.get(
            f'{self.base_url}/meme', headers=self.headers
        )
        return self.response
