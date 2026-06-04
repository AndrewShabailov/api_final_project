import requests
import allure
from endpoints.base_meme import BaseMeme


class ReadMeme(BaseMeme):

    @allure.step('Send GET request for reading all memes')
    def read_all_meme(self):
        self.response = requests.get(
            f'{self.base_url}/meme', headers=self.headers
        )
        return self.response

    @allure.step('Send GET request for reading specific meme')
    def read_specific_meme(self, meme_id):
        self.response = requests.get(
            f'{self.base_url}/meme/{meme_id}', headers=self.headers
        )
        return self.response

    @allure.step('Send GET request to validate token')
    def check_token(self):
        self.response = requests.get(
            f'{self.base_url}/meme', headers=self.headers
        )
        return self.response
